from env_interaction_sim import run_simulation
import pandas as pd
def run_single_simulation_experiments(bot_counts, max_moves):
    """
    Runs a single simulation for each bot configuration.
    """
    for num_bots in bot_counts:
        collected_dirt = run_simulation(NUM_BOTS=num_bots, MAX_MOVES=max_moves)
        print(f"[Single] {num_bots} bot(s): Collected {collected_dirt} dirt.")


def run_multiple_trials(bot_counts, num_trials, max_moves):
    def run_multiple_trials(bot_counts, num_trials, max_moves):
        """
        Runs multiple trials per bot configuration and collects results.
        Returns a list of dictionaries, each containing results for one trial.
        """
    results_list = []  # Initialize an empty list to store results

    for num_bots in bot_counts:
        print(f"\n[Configuration] Testing with {num_bots} bot(s)...")
        for trial_index in range(1, num_trials + 1):
            # Run the simulation for the current configuration and trial
            # Assuming run_simulation returns the amount of dirt collected
            collected_dirt = run_simulation(NUM_BOTS=num_bots, MAX_MOVES=max_moves)

            # Print immediate feedback (optional, but helpful)
            print(f"[Trial] {num_bots} bot(s), Trial {trial_index}/{num_trials}: Collected {collected_dirt} dirt.")

            # Create a dictionary for this run's data
            run_data = {
                'num_bots': num_bots,
                'trial': trial_index,
                'dirt_collected': collected_dirt
            }

            # Append the dictionary to our results list
            results_list.append(run_data)

        print("-" * 30) # Separator between configurations

    return results_list # Return the collected data



if __name__ == "__main__":
    # Define experiment parameters (use consistent names)
    bot_counts_to_test = [1, 5]   # Number of bots per configuration
    trials_per_config = 2                # Number of trials for each bot count
    moves_limit = 200                    # Max moves per simulation run

    print("=" * 50 + "\nSimulation Experiment Suite - Activity 4\n" +
          f"Bot Counts: {bot_counts_to_test}\n" +
          f"Trials per Count: {trials_per_config}\n" +
          f"Max Moves per Run: {moves_limit}\n" +
          "=" * 50)

    # --- Run multiple trials and collect results ---
    print("\n--- Running Multiple Trials & Collecting Results ---")
    # Assuming run_multiple_trials is defined above or imported
    all_results_data = run_multiple_trials(
        bot_counts=bot_counts_to_test,
        num_trials=trials_per_config,
        max_moves=moves_limit
    )

    print("\n--- Collected Results (List of Dictionaries) ---")
    print(all_results_data)

    results_df = pd.DataFrame(all_results_data)
    output_filename = "simulation_results.xlsx"
    results_df.to_excel(output_filename, index=False)