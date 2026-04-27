import argparse
import csv
import glob
import os
import re

import ale_py
import gymnasium as gym
import numpy as np
from stable_baselines3 import DQN, PPO
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.vec_env import VecFrameStack

gym.register_envs(ale_py)

ENV_IDS = {
    "qbert":      "QbertNoFrameskip-v4",
    "donkeykong": "ALE/DonkeyKong-v5",
}

CSV_FIELDS = [
    "run_id", "algo", "env", "checkpoint", "steps",
    "mean_reward", "std_reward", "min_reward", "max_reward", "mean_ep_length",
]


def parse_args():
    parser = argparse.ArgumentParser(description="Evaluate saved SB3 checkpoints on an Atari env.")
    parser.add_argument("--algo", choices=["dqn", "ppo"], required=True)
    parser.add_argument("--env", choices=["qbert", "donkeykong"], required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--checkpoint-dir", type=str,
                       help="Evaluate all checkpoints in this directory")
    group.add_argument("--checkpoint", type=str,
                       help="Evaluate a single checkpoint .zip file")
    parser.add_argument("--episodes", type=int, default=20,
                        help="Number of evaluation episodes per checkpoint (default: 20)")
    parser.add_argument("--output", type=str, default="results/evaluation.csv",
                        help="Path to output CSV (rows are appended)")
    return parser.parse_args()


def extract_steps(path):
    name = os.path.basename(path)
    match = re.search(r"checkpoint_(\d+)_steps", name)
    if match:
        return int(match.group(1))
    if "final_model" in name:
        return float("inf")
    return -1


def find_checkpoints(directory):
    paths = sorted(
        glob.glob(os.path.join(directory, "checkpoint_*_steps.zip")),
        key=extract_steps,
    )
    final = os.path.join(directory, "final_model.zip")
    if os.path.exists(final):
        paths.append(final)
    return paths


def run_evaluation(checkpoint_path, algo, env_key, n_episodes):
    cls = DQN if algo == "dqn" else PPO
    eval_env = make_atari_env(ENV_IDS[env_key], n_envs=1, seed=42)
    eval_env = VecFrameStack(eval_env, n_stack=4)
    model = cls.load(checkpoint_path, env=eval_env, device="cpu")

    episode_rewards, episode_lengths = evaluate_policy(
        model, eval_env,
        n_eval_episodes=n_episodes,
        deterministic=True,
        return_episode_rewards=True,
    )
    eval_env.close()

    return {
        "mean_reward":    float(np.mean(episode_rewards)),
        "std_reward":     float(np.std(episode_rewards)),
        "min_reward":     float(np.min(episode_rewards)),
        "max_reward":     float(np.max(episode_rewards)),
        "mean_ep_length": float(np.mean(episode_lengths)),
    }


def append_csv(output_path, row):
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    file_exists = os.path.exists(output_path)
    with open(output_path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)


def main():
    args = parse_args()

    checkpoints = (
        find_checkpoints(args.checkpoint_dir)
        if args.checkpoint_dir
        else [args.checkpoint]
    )

    if not checkpoints:
        print(f"No checkpoints found.")
        return

    run_id = f"{args.algo}_{args.env}"
    print(f"\nRun: {run_id}  |  {len(checkpoints)} checkpoint(s)  |  {args.episodes} episodes each")
    print("-" * 60)

    for ckpt in checkpoints:
        name = os.path.basename(ckpt).replace(".zip", "")
        steps = extract_steps(ckpt)
        steps_label = "final" if steps == float("inf") else str(steps)

        print(f"  {name:<45} ", end="", flush=True)
        metrics = run_evaluation(ckpt, args.algo, args.env, args.episodes)
        print(f"reward: {metrics['mean_reward']:7.1f} ± {metrics['std_reward']:.1f}")

        append_csv(args.output, {
            "run_id": run_id,
            "algo":   args.algo,
            "env":    args.env,
            "checkpoint": name,
            "steps":  steps_label,
            **metrics,
        })

    print(f"\nResults saved to: {args.output}")


if __name__ == "__main__":
    main()
