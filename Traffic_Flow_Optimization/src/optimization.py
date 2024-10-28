# src/optimization.py

import numpy as np
import random

def initialize_population(size, num_signals):
    """Generate initial population for Genetic Algorithm."""
    return [np.random.randint(0, 60, num_signals) for _ in range(size)]

def fitness_function(schedule, traffic_data):
    """Evaluate the fitness of each schedule based on congestion reduction."""
    # Example: Lower congestion and average wait time
    congestion_score = np.mean(traffic_data * schedule)
    return 1 / (1 + congestion_score)

def select_parents(population, fitness_scores):
    """Select parents for reproduction."""
    parents = random.choices(population, weights=fitness_scores, k=2)
    return parents

def crossover(parent1, parent2):
    """Crossover parents to produce offspring."""
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2

def mutate(schedule):
    """Apply mutation to the schedule."""
    mutation_index = random.randint(0, len(schedule) - 1)
    schedule[mutation_index] = random.randint(0, 60)
    return schedule

def run_genetic_algorithm(traffic_data, num_generations=50, population_size=100):
    """Optimize traffic signals using a genetic algorithm."""
    num_signals = traffic_data.shape[1]
    population = initialize_population(population_size, num_signals)
    
    for generation in range(num_generations):
        fitness_scores = [fitness_function(schedule, traffic_data) for schedule in population]
        new_population = []
        
        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population, fitness_scores)
            child1, child2 = crossover(parent1, parent2)
            new_population.extend([mutate(child1), mutate(child2)])
        
        population = new_population
    
    best_schedule = max(population, key=lambda s: fitness_function(s, traffic_data))
    return best_schedule
