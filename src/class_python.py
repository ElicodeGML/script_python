# Copied and normalized Python script from scripts_/class_python.py
# Cleaned variable names and removed demo prints for module usage
import tkinter as tk
from tkinter import messagebox, scrolledtext
import numpy as np


class Car:
    """Simple car class with speed management."""
    
    def __init__(self, p_brand, p_color, p_speed=0):
        """Initialize a car with brand, color, and speed."""
        self.brand = p_brand
        self.color = p_color
        self.speed = p_speed
    
    def accelerate(self, p_speed):
        """Increase car speed."""
        self.speed += p_speed

    def decelerate(self, p_speed):
        """Decrease car speed (minimum 0)."""
        self.speed -= p_speed
        if self.speed < 0:
            self.speed = 0


class Game:
    """Game class to manage scoring rounds with multiple players."""

    def __init__(self, target_score=None):
        self.players = {}
        self.target_score = target_score if target_score is not None else 0
        self.game_over = False
        self._current_round_number = 0
        self.round_details = [] # Stores {'round_num': X, 'round_scores': {player: score_this_round}, 'round_winner_names': [], 'round_max_score': Y}

    def set_target_score(self, score):
        if not isinstance(score, int) or score <= 0:
            raise ValueError("Le score cible doit être un entier positif.")
        self.target_score = score

    def add_player(self, player_name):
        if not player_name.strip():
            return "Le nom du joueur ne peut pas être vide."
        if player_name in self.players:
            return "Ce nom de joueur existe déjà."
        self.players[player_name] = []
        return None # No error

    def add_scores_round(self, scores_for_this_round_input):
        if self.game_over:
            return True, None # Game already over, no error

        self._current_round_number += 1
        scores_for_this_round = {}
        for player_name, score_str in scores_for_this_round_input.items():
            try:
                scores_for_this_round[player_name] = int(score_str)
            except ValueError:
                return False, f"Score invalide pour {player_name}. Veuillez entrer un nombre entier."

        for player_name, score in scores_for_this_round.items():
            self.players[player_name].append(score)

        current_round_max_score = 0
        current_round_winner_names = []
        overall_leader_names = []
        overall_max_score = 0

        game_won_this_round = False
        for player_name, scores_list in self.players.items():
            current_total = sum(scores_list)

            round_score = scores_for_this_round.get(player_name, 0)
            if round_score > current_round_max_score:
                current_round_max_score = round_score
                current_round_winner_names = [player_name]
            elif round_score == current_round_max_score:
                current_round_winner_names.append(player_name)

            if current_total > overall_max_score:
                overall_max_score = current_total
                overall_leader_names = [player_name]
            elif current_total == overall_max_score:
                overall_leader_names.append(player_name)

            if current_total >= self.target_score:
                self.game_over = True
                game_won_this_round = True

        self.round_details.append({
            'round_num': self._current_round_number,
            'round_scores': scores_for_this_round,
            'round_winner_names': current_round_winner_names,
            'round_max_score': current_round_max_score
        })

        return game_won_this_round, None

# Demo GUI class omitted in module copy; keep GUI code as separate script if needed
