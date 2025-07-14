import math
from scipy.stats import norm

# Black-Scholes formula for European Call Option pricing
def black_scholes_call(S0, X, T, r, sigma):
    """
    S0: Current stock price
    X: Strike price of the option
    T: Time to expiration (in years)
    r: Risk-free interest rate (annual rate)
    sigma: Volatility of the stock (annualized)
    Returns the price of the European call option.
    """
    # Calculate d1 and d2
    d1 = (math.log(S0 / X) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    # Calculate the option price
    call_price = S0 * norm.cdf(d1) - X * math.exp(-r * T) * norm.cdf(d2)
    return call_price

# Example usage:
S0 = 50 # Current stock price
X = 95 # Strike price
T = 1 # Time to expiration (1 year)
r = 0.05 # Risk-free interest rate (5%)
sigma = 0.2 # Volatility (20%)

# Calculate the call option price
call_option_price = black_scholes_call(S0, X, T, r, sigma)
print(f"European Call Option Price: ${call_option_price:.2f}")
