import numpy as np

# Paramètres de base
S0 = 100             # Prix initial du sous-jacent
K = 100              # Strike
barrier = 100        # Barrière d’autocall
T = 3                # Durée en années
r = 0.01             # Taux sans risque
sigma = 0.2          # Volatilité
nb_obs = 3           # Observations annuelles
coupon = 0.08        # Coupon annuel
simulations = 10000  # Nombre de trajectoires simulées

np.random.seed(42)
dt = 1/nb_obs
discount_factor = np.exp(-r * T)

def simulate_autocall_payoff():
    S = S0
    for i in range(1, nb_obs + 1):
        z = np.random.normal()
        S *= np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)
        if S >= barrier:
            return coupon * i * np.exp(-r * i * dt)  # paiement anticipé
    return np.exp(-r * T) * max(S - K, 0)  # remboursement à maturité

# Simulation de Monte Carlo
payoffs = [simulate_autocall_payoff() for _ in range(simulations)]
price = np.mean(payoffs)

print(f"Prix estimé de l'autocall : {price:.4f}")
