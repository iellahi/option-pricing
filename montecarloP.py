import numpy as np

# Monte Carlo simulation for European Call Option pricing
def monte_carlo_call(S0, K, T, r, sigma, num_simulations):
    # Simulate asset paths at time T using Geometric Brownian Motion
    np.random.seed(42) # For reproducibility
    Z = np.random.normal(0, 1, num_simulations) # Standard normal random variables
    ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * Z)
    # Compute the payoff for each simulation
    payoffs = np.maximum(ST - K, 0)
    # Discount the average payoff to present value
    call_price = np.exp(-r * T) * np.mean(payoffs)
    return call_price, payoffs

# Example usage:
S0 = 100 # Current stock price
K = 95 # Strike price
T = 1 # Time to expiration (1 year)
r = 0.05 # Risk-free interest rate (5%)
sigma = 0.2 # Volatility (20%)
num_simulations = 100 # Number of simulations

# Calculate the call option price using Monte Carlo
call_option_price_monte_carlo, payoffs = monte_carlo_call(S0, K, T, r, sigma, num_simulations)
print(f"European Call Option Price (Monte Carlo): ${call_option_price_monte_carlo:.2f}")
