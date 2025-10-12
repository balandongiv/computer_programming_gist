from env_interaction_sim import run_simulation

def run_single_simulation_experiments(bot_counts, max_moves):
    """
    Runs a single simulation for each bot configuration.
    """
    for num_bots in bot_counts:
        collected_dirt = run_simulation(NUM_BOTS=num_bots, MAX_MOVES=max_moves)
        print(f"[Single] {num_bots} bot(s): Collected {collected_dirt} dirt.")


def run_multiple_trials(bot_counts, num_trials, max_moves):
    """
    Runs multiple trials per bot configuration.
    """
    pass


if __name__ == "__main__":  # main
    # Define experiment parameters
    bot_counts_to_test = [1, 5, 10, 20]   # Example list
    trials_per_config = 3                # Example number of trials
    moves_limit = 200                    # Example move limit



    # --- Optional: Run single simulations first ---
    # run_single_simulation_experiments(bot_counts_to_test, moves_limit)

    # --- Run multiple trials ---
    run_multiple_trials(
        bot_counts=bot_counts_to_test,
        num_trials=trials_per_config,
        max_moves=moves_limit
    )
