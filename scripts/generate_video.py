import argparse
import os

import ale_py
import gymnasium as gym
from stable_baselines3 import DQN, PPO
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.vec_env import VecFrameStack, VecVideoRecorder

gym.register_envs(ale_py)

ENV_IDS = {
    "qbert":      "QbertNoFrameskip-v4",
    "donkeykong": "ALE/DonkeyKong-v5",
}


def parse_args():
    parser = argparse.ArgumentParser(description="Record gameplay video from a saved SB3 model.")
    parser.add_argument("--checkpoint", type=str, required=True,
                        help="Path to .zip checkpoint")
    parser.add_argument("--algo", choices=["dqn", "ppo"], required=True)
    parser.add_argument("--env", choices=["qbert", "donkeykong"], required=True)
    parser.add_argument("--steps", type=int, default=3000,
                        help="Number of steps to record (default: 3000)")
    parser.add_argument("--output-dir", type=str, default="videos",
                        help="Directory to save video (default: videos/)")
    parser.add_argument("--label", type=str, default=None,
                        help="Label for the video filename, e.g. 'early', 'mid', 'final'")
    return parser.parse_args()


def main():
    args = parse_args()

    cls = DQN if args.algo == "dqn" else PPO

    checkpoint_name = os.path.basename(args.checkpoint).replace(".zip", "")
    label = args.label or checkpoint_name
    video_name = f"{args.algo}_{args.env}_{label}"

    os.makedirs(args.output_dir, exist_ok=True)

    vec_env = make_atari_env(
        ENV_IDS[args.env],
        n_envs=1,
        seed=0,
        env_kwargs={"render_mode": "rgb_array"},
    )
    vec_env = VecFrameStack(vec_env, n_stack=4)
    vec_env = VecVideoRecorder(
        vec_env,
        video_folder=args.output_dir,
        record_video_trigger=lambda x: x == 0,
        video_length=args.steps,
        name_prefix=video_name,
    )

    model = cls.load(args.checkpoint, env=vec_env, device="cpu")

    obs = vec_env.reset()
    for _ in range(args.steps):
        action, _ = model.predict(obs, deterministic=True)
        obs, _, done, _ = vec_env.step(action)

    vec_env.close()
    print(f"Video saved to: {args.output_dir}/{video_name}-step-0-to-step-{args.steps}.mp4")


if __name__ == "__main__":
    main()
