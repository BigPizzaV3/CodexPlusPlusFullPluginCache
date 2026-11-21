# Primary technical sources

Checked 2026-10-16. Match installed versions before prescribing APIs.

- [OpenAI Spinning Up: RL concepts](https://spinningup.openai.com/en/latest/spinningup/rl_intro.html): states, actions, policies, rewards and sequential interaction. Use for concepts, not as a current managed-service compatibility guarantee.
- [Gymnasium environment API](https://gymnasium.farama.org/api/env/): observation/action spaces and terminated versus truncated episodes.
- [Stable Baselines3 algorithm support](https://stable-baselines3.readthedocs.io/en/master/guide/algos.html): verify action-space support and installed version. This page also warns that total_timesteps can be exceeded by rollout batching; do not call it a hard spending limit.
- [Vowpal Wabbit contextual bandits](https://vowpalwabbit.org/docs/vowpal_wabbit/python/latest/tutorials/python_Contextual_bandits_and_Vowpal_Wabbit.html): selected-action feedback, context, policies and evaluation approaches.

Illustrative choice, not a default recommendation: discrete action tasks may fit algorithms that require discrete actions, while continuous actions need appropriate support. A pretrained predictor or language-model checkpoint needs architecture-specific integration, not an arbitrary rename. Verify a hosted provider's current supported models and training methods separately before suggesting a managed training job.
