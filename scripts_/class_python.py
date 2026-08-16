class Car:
    
    def __init__(self, p_brand, p_color, p_speed = 0):
        self.brand = p_brand
        self.color = p_color
        self.speed = p_speed
    def accelerate(self , p_speed):
        self.speed += p_speed

    def decelerate(self , p_speed):
        self.speed -= p_speed
        if self.speed < 0:
            self.speed = 0

blue_car = Car("BMW", "blue", 20)
red_car = Car("Peugot", "red")

blue_car.color = "blue"
red_car.color = "red"

print(blue_car.speed)
print(red_car.speed)

blue_car.accelerate(20)
print(blue_car.speed)
print(red_car.speed)

blue_car.decelerate(10)
print(blue_car.speed)
print(red_car.speed)

blue_car.decelerate(100)
print(blue_car.speed)
print(red_car.speed)

import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext
import numpy as np


class Game:
    import tkinter as tk
    from tkinter import simpledialog, messagebox, scrolledtext
    import numpy as np

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

    def get_current_scores(self):
        return {name: sum(scores) for name, scores in self.players.items()}

    def get_overall_leader_info(self):
        if not self.players:
            return [], 0
        final_scores = self.get_current_scores()
        if not final_scores:
            return [], 0

        max_total_score = 0
        leader_names = []
        for player_name, total_score in final_scores.items():
            if total_score > max_total_score:
                max_total_score = total_score
                leader_names = [player_name]
            elif total_score == max_total_score:
                leader_names.append(player_name)
        return leader_names, max_total_score

    def get_round_winner_info(self, round_num=None):
        if not self.round_details:
            return [], 0, {}

        if round_num is None:
            # Get info for the latest round
            latest_round = self.round_details[-1]
        else:
            latest_round = next((rd for rd in self.round_details if rd['round_num'] == round_num), None)
            if not latest_round: return [], 0, {}

        return latest_round['round_winner_names'], latest_round['round_max_score'], latest_round['round_scores']

    def get_stats_report(self):
        report = ""
        if not self.players:
            report += "Aucun joueur n'a participé à cette partie.\n"
            return report

        final_scores = {name: sum(scores) for name, scores in self.players.items()}
        if not final_scores:
            report += "Aucun score enregistré.\n"
            return report

        report += "\n=== Récapitulatif des manches ===\n\n" # Section start
        if not self.round_details:
            report += "Aucune manche n'a été jouée.\n"
        else:
            for rd in self.round_details:
                round_num = rd['round_num']
                round_winner_names = rd['round_winner_names']
                round_max_score = rd['round_max_score']
                round_scores = rd['round_scores']
                if round_winner_names and round_max_score > 0:
                    report += f"Manche {round_num} : Gagnant(s) = {', '.join(round_winner_names)} ({round_max_score} points dans la manche). Scores: {round_scores}\n"
                else:
                    report += f"Manche {round_num} : Aucun gagnant de manche (scores: {round_scores}).\n"
            report += "\n" # Add a newline after round recap

        max_total_score = 0
        winner_names = []
        all_scores_flat = []

        report += "\n=== Scores Totaux par Joueur ===\n\n" # Section start
        for player_name, total_score in final_scores.items():
            player_round_scores = self.players[player_name]
            report += f"{player_name}: Total {total_score} (Scores par tour: {player_round_scores})\n"
            all_scores_flat.extend(player_round_scores)

            if total_score > max_total_score:
                max_total_score = total_score
                winner_names = [player_name]
            elif total_score == max_total_score:
                winner_names.append(player_name)

            if player_round_scores:
                player_avg = np.mean(player_round_scores)
                player_std = np.std(player_round_scores)
                player_min = np.min(player_round_scores)
                player_max = np.max(player_round_scores)
                report += f"  -> Stats de {player_name}: Moyenne={player_avg:.2f}, Écart-type={player_std:.2f}, Min={player_min}, Max={player_max}\n"
            else:
                report += f"  -> {player_name} n'a pas encore de scores de tour enregistrés.\n"
            report += "\n" # Add a newline after each player's stats

        report += "\n=== Résultat Final ===\n\n" # Section start
        if self.game_over:
            report += f"Le gagnant est : {', '.join(winner_names)} avec un score de {max_total_score} !\n"
        else:
            report += "La partie n'est pas encore terminée ou aucun gagnant n'a été déterminé selon le score cible.\n"
            report += f"Le joueur avec le score le plus élevé est : {', '.join(winner_names)} avec un score de {max_total_score}.\n"
        report += "\n" # Add a newline after final result

        if all_scores_flat:
            report += "\n=== Statistiques Globales des Scores par Tour ===\n\n" # Section start
            overall_avg = np.mean(all_scores_flat)
            overall_std = np.std(all_scores_flat)
            overall_min = np.min(all_scores_flat)
            overall_max = np.max(all_scores_flat)
            report += f"Moyenne globale des scores par tour: {overall_avg:.2f}\n"
            report += f"Écart-type global des scores par tour: {overall_std:.2f}\n"
            report += f"Score minimum global par tour: {overall_min}\n"
            report += f"Score maximum global par tour: {overall_max}\n"

            player_min_score_round_str = []
            player_max_score_round_str = []
            if all_scores_flat:
                min_score_val = float('inf')
                max_score_val = float('-inf')

                for p_name, p_scores in self.players.items():
                    if p_scores:
                        current_min_p = min(p_scores)
                        current_max_p = max(p_scores)

                        if current_min_p < min_score_val:
                            min_score_val = current_min_p
                            player_min_score_round_str = [f"{p_name} ({current_min_p})"]
                        elif current_min_p == min_score_val:
                            player_min_score_round_str.append(f"{p_name} ({current_min_p})")

                        if current_max_p > max_score_val:
                            max_score_val = current_max_p
                            player_max_score_round_str = [f"{p_name} ({current_max_p})"]
                        elif current_max_p == max_score_val:
                            player_max_score_round_str.append(f"{p_name} ({current_max_p})")

                report += f"Joueur(s) avec le score le plus bas par tour: {', '.join(player_min_score_round_str)}\n"
                report += f"Joueur(s) avec le score le plus haut par tour: {', '.join(player_max_score_round_str)}\n"
            report += "\n" # Add a newline after global stats
        return report


class GameGUI:
    import tkinter as tk
    from tkinter import simpledialog, messagebox, scrolledtext
    import numpy as np

    # Color Palette
    BG_COLOR = "#F0F0F0"  # Light Gray
    FRAME_BG_COLOR = "#FFFFFF"  # White
    BUTTON_COLOR = "#4CAF50" # Green
    BUTTON_ACTIVE_COLOR = "#45A049"
    BUTTON_TEXT_COLOR = "white"
    LABEL_TEXT_COLOR = "#333333" # Dark Grey
    ENTRY_BG_COLOR = "white"
    HIGHLIGHT_COLOR = "#CA2D4F" # Gold for round winner
    WINNER_COLOR = "#008000" # Darker Green for overall leader
    GAME_OVER_COLOR = "#009CCC" # Dark Red
    FONT_FAMILY = "Helvetica"

    def __init__(self, master):
        self.master = master
        master.title("Jeu de Score")
        master.geometry("1000x700") # Increased initial size
        master.minsize(800, 600) # Minimum size
        master.configure(bg=self.BG_COLOR)

        self.game = Game() # Initialize game without target score initially
        self.player_entries = {}
        self.score_entries = {}
        self._player_entry_widgets_list = [] # New: to keep order for focus movement
        self._score_entry_widgets_list = [] # New: to keep order for score entry focus movement
        self.num_players_input_var = tk.StringVar(master, value="2") # Default value for num players
        self.target_score_input_var = tk.StringVar(master, value="100") # Default value for target score

        self.create_widgets()

    def create_widgets(self):
        # --- Game Setup Frame ---
        self.setup_frame = tk.LabelFrame(self.master, text="Configuration du Jeu", padx=15, pady=15,
                                         bg=self.FRAME_BG_COLOR, fg=self.LABEL_TEXT_COLOR, font=(self.FONT_FAMILY, 14, "bold"))
        self.setup_frame.pack(pady=15, padx=15, fill="both", expand=True)
        self.setup_frame.grid_columnconfigure(1, weight=1) # Allow entry column to expand

        tk.Label(self.setup_frame, text="Score Cible:", bg=self.FRAME_BG_COLOR, fg=self.LABEL_TEXT_COLOR, font=(self.FONT_FAMILY, 11)).grid(row=0, column=0, sticky="w", pady=5)
        self.target_score_entry = tk.Entry(self.setup_frame, textvariable=self.target_score_input_var, bg=self.ENTRY_BG_COLOR, fg=self.LABEL_TEXT_COLOR, font=(self.FONT_FAMILY, 11))
        self.target_score_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
        self.target_score_entry.bind('<Return>', self.set_target_score_event) # Bind Enter key
        self.set_target_score_btn = tk.Button(self.setup_frame, text="Définir Score Cible", command=self.set_target_score,
                                            bg=self.BUTTON_COLOR, fg=self.BUTTON_TEXT_COLOR, activebackground=self.BUTTON_ACTIVE_COLOR, font=(self.FONT_FAMILY, 11, "bold"))
        self.set_target_score_btn.grid(row=0, column=2, padx=10, pady=5)

        tk.Label(self.setup_frame, text="Nombre de Joueurs:", bg=self.FRAME_BG_COLOR, fg=self.LABEL_TEXT_COLOR, font=(self.FONT_FAMILY, 11)).grid(row=1, column=0, sticky="w", pady=5)
        self.num_players_entry = tk.Entry(self.setup_frame, textvariable=self.num_players_input_var, bg=self.ENTRY_BG_COLOR, fg=self.LABEL_TEXT_COLOR, font=(self.FONT_FAMILY, 11))
        self.num_players_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=5)
        self.num_players_entry.bind('<Return>', self.create_player_name_inputs_event) # Bind Enter key
        self.create_players_btn = tk.Button(self.setup_frame, text="Créer Joueurs", command=self.create_player_name_inputs,
                                            bg=self.BUTTON_COLOR, fg=self.BUTTON_TEXT_COLOR, activebackground=self.BUTTON_ACTIVE_COLOR, font=(self.FONT_FAMILY, 11, "bold"))
        self.create_players_btn.grid(row=1, column=2, padx=10, pady=5)

        self.player_name_frame = tk.Frame(self.setup_frame, bg=self.FRAME_BG_COLOR)
        self.player_name_frame.grid(row=2, column=0, columnspan=3, sticky="ew", pady=10)
        self.player_name_frame.grid_columnconfigure(1, weight=1)

        self.start_game_btn = tk.Button(self.setup_frame, text="Démarrer la Partie", command=self.start_game, state=tk.DISABLED,
                                       bg="#CCCCCC", fg=self.BUTTON_TEXT_COLOR, activebackground=self.BUTTON_ACTIVE_COLOR, font=(self.FONT_FAMILY, 13, "bold"))
        self.start_game_btn.grid(row=3, column=0, columnspan=3, pady=15)

        # --- Game Play Frame (initially hidden) ---
        self.game_play_frame = tk.LabelFrame(self.master, text="Jouer le Tour", padx=15, pady=15,
                                              bg=self.FRAME_BG_COLOR, fg=self.LABEL_TEXT_COLOR, font=(self.FONT_FAMILY, 14, "bold"))

        self.current_round_label = tk.Label(self.game_play_frame, text="Tour: 0", bg=self.FRAME_BG_COLOR, fg=self.LABEL_TEXT_COLOR, font=(self.FONT_FAMILY, 13, "bold"))
        self.current_round_label.pack(pady=10)

        self.current_scores_label = tk.Label(self.game_play_frame, text="Scores Actuels: ", bg=self.FRAME_BG_COLOR, fg=self.LABEL_TEXT_COLOR, font=(self.FONT_FAMILY, 11))
        self.current_scores_label.pack(pady=5)

        self.round_winner_label = tk.Label(self.game_play_frame, text="Gagnant(s) de la dernière Manche: ", bg=self.FRAME_BG_COLOR, fg=self.LABEL_TEXT_COLOR, font=(self.FONT_FAMILY, 11))
        self.round_winner_label.pack(pady=2)

        self.overall_leader_label = tk.Label(self.game_play_frame, text="Leader(s) Général(aux):\n", bg=self.FRAME_BG_COLOR, fg=self.LABEL_TEXT_COLOR, font=(self.FONT_FAMILY, 11))
        self.overall_leader_label.pack(pady=2)

        self.score_input_frame = tk.Frame(self.game_play_frame, bg=self.FRAME_BG_COLOR)
        self.score_input_frame.pack(pady=10, fill="x", expand=False)

        self.add_scores_btn = tk.Button(self.game_play_frame, text="Ajouter Scores de Tour", command=self.add_scores_round,
                                         state=tk.DISABLED, bg=self.BUTTON_COLOR, fg=self.BUTTON_TEXT_COLOR, activebackground=self.BUTTON_ACTIVE_COLOR, font=(self.FONT_FAMILY, 11, "bold"))
        self.add_scores_btn.pack(pady=15)
        # Removed global Enter key binding for score input
        # self.master.bind('<Return>', self.add_scores_round_event)

        # --- Game Over / Stats Frame (initially hidden) ---
        self.stats_frame = tk.LabelFrame(self.master, text="Résultats de la Partie", padx=15, pady=15,
                                         bg=self.FRAME_BG_COLOR, fg=self.LABEL_TEXT_COLOR, font=(self.FONT_FAMILY, 14, "bold"))

        self.game_over_label = tk.Label(self.stats_frame, text="Partie Terminée!", font=(self.FONT_FAMILY, 16, "bold"), fg=self.GAME_OVER_COLOR, bg=self.FRAME_BG_COLOR)
        self.game_over_label.pack(pady=10)

        self.stats_text = scrolledtext.ScrolledText(self.stats_frame, width=80, height=20, wrap=tk.WORD,
                                                  bg=self.ENTRY_BG_COLOR, fg=self.LABEL_TEXT_COLOR, font=("Consolas", 10))
        self.stats_text.pack(pady=10, fill="both", expand=True)

        self.new_game_btn = tk.Button(self.stats_frame, text="Nouvelle Partie", command=self.reset_game,
                                       bg=self.BUTTON_COLOR, fg=self.BUTTON_TEXT_COLOR, activebackground=self.BUTTON_ACTIVE_COLOR, font=(self.FONT_FAMILY, 11, "bold"))
        self.new_game_btn.pack(pady=15)

    # Event handler for Enter key on target_score_entry
    def set_target_score_event(self, event=None):
        self.set_target_score()
        # After setting target score, move focus to num_players_entry
        self.num_players_entry.focus_set()

    def set_target_score(self):
        try:
            target = int(self.target_score_input_var.get())
            self.game.set_target_score(target)
            messagebox.showinfo("Succès", f"Score cible défini à {target}.", parent=self.master)
            self.update_start_game_button_state()
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre entier positif pour le score cible.", parent=self.master)

    # Event handler for Enter key on num_players_entry
    def create_player_name_inputs_event(self, event=None):
        self.create_player_name_inputs()

    def create_player_name_inputs(self):
        for widget in self.player_name_frame.winfo_children():
            widget.destroy()
        self.player_entries = {}
        self._player_entry_widgets_list = [] # New: to keep order for focus movement

        try:
            num_players = int(self.num_players_input_var.get())
            if num_players <= 0:
                messagebox.showerror("Erreur", "Le nombre de joueurs doit être positif.", parent=self.master)
                return
            if num_players > 10: # Arbitrary limit for UI layout
                messagebox.showwarning("Attention", "Trop de joueurs peuvent rendre l'affichage encombrant. Considérez de réduire le nombre.", parent=self.master)

            for i in range(num_players):
                tk.Label(self.player_name_frame, text=f"Nom Joueur {i+1}:", bg=self.FRAME_BG_COLOR, fg=self.LABEL_TEXT_COLOR, font=(self.FONT_FAMILY, 11)).grid(row=i, column=0, sticky="w", pady=2)
                entry = tk.Entry(self.player_name_frame, bg=self.ENTRY_BG_COLOR, fg=self.LABEL_TEXT_COLOR, font=(self.FONT_FAMILY, 11))
                entry.grid(row=i, column=1, sticky="ew", padx=10, pady=2)
                entry.bind('<Return>', lambda event, current_idx=i: self._on_player_name_entry_return(event, current_idx)) # NEW BINDING
                self.player_entries[f"Player_{i+1}"] = entry
                self._player_entry_widgets_list.append(entry) # Add to ordered list

            # After creating player name inputs, set focus to the first one
            if self._player_entry_widgets_list:
                self._player_entry_widgets_list[0].focus_set()

            # Add a button to confirm player names and add to game object
            self.confirm_players_btn = tk.Button(self.player_name_frame, text="Confirmer Noms", command=self.confirm_player_names,
                                                bg=self.BUTTON_COLOR, fg=self.BUTTON_TEXT_COLOR, activebackground=self.BUTTON_ACTIVE_COLOR, font=(self.FONT_FAMILY, 11, "bold"))
            self.confirm_players_btn.grid(row=num_players, column=0, columnspan=2, pady=10)

        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre entier pour le nombre de joueurs.", parent=self.master)

    def _on_player_name_entry_return(self, event, current_idx):
        # If it's the last entry, call confirm_player_names
        if current_idx == len(self._player_entry_widgets_list) - 1:
            self.confirm_player_names()
        else:
            # Move focus to the next entry
            self._player_entry_widgets_list[current_idx + 1].focus_set()

    # Event handler for Enter key on player name entries (this was the old one, no longer directly used)
    def confirm_player_names_event(self, event=None):
        # This method is no longer bound directly to individual entry <Return> keys
        # It's kept for consistency if needed elsewhere, but _on_player_name_entry_return handles sequential focus
        self.confirm_player_names()

    def confirm_player_names(self):
        temp_players = {}
        # Validate names first
        for player_id, entry_widget in self.player_entries.items():
            player_name = entry_widget.get().strip()
            if not player_name:
                messagebox.showerror("Erreur", "Le nom d'un joueur ne peut pas être valide.", parent=self.master)
                return
            if player_name in temp_players:
                messagebox.showerror("Erreur", f"Le nom '{player_name}' est dupliqué dans cette liste. Veuillez en choisir un autre.", parent=self.master)
                return
            # This check might be redundant if game.players is cleared, but good for robustness
            if player_name in self.game.players and self.game.players[player_name]:
                messagebox.showerror("Erreur", f"Le nom '{player_name}' existe déjà dans la partie. Veuillez en choisir un autre.", parent=self.master)
                return
            temp_players[player_name] = []

        # If all names are valid, then actually add them to the game
        self.game.players = {} # Clear existing players before adding the new confirmed ones
        for player_id, entry_widget in self.player_entries.items():
            player_name = entry_widget.get().strip()
            error = self.game.add_player(player_name) # This will always be None now due to prior checks
            if error: # Should not happen, but for safety
                 messagebox.showerror("Erreur interne", error, parent=self.master)
                 return

        messagebox.showinfo("Succès", f"Joueurs confirmés : {', '.join(self.game.players.keys())}", parent=self.master)
        self.update_start_game_button_state()

        # If the game is now ready, start it automatically
        if str(self.start_game_btn['state']) == 'normal':
            self.start_game()

    def update_start_game_button_state(self):
        if self.game.target_score > 0 and self.game.players:
            self.start_game_btn.config(state=tk.NORMAL, bg=self.BUTTON_COLOR)
        else:
            self.start_game_btn.config(state=tk.DISABLED, bg="#CCCCCC") # Gray out when disabled

    def start_game(self):
        if not self.game.players:
            messagebox.showerror("Erreur", "Veuillez créer et confirmer les joueurs d'abord.", parent=self.master)
            return
        if self.game.target_score == 0:
            messagebox.showerror("Erreur", "Veuillez définir un score cible d'abord.", parent=self.master)
            return

        self.setup_frame.pack_forget()
        self.game_play_frame.pack(pady=15, padx=15, fill="both", expand=True)
        self.add_scores_btn.config(state=tk.NORMAL)
        self.update_game_display()
        # Set focus to the first score entry if available for immediate typing
        if self.score_entries:
            list(self.score_entries.values())[0].focus_set()

    # Event handler for Enter key on individual score entries
    def _on_score_entry_return(self, event, current_idx):
        # Try to move focus to the next score entry
        if current_idx < len(self._score_entry_widgets_list) - 1:
            self._score_entry_widgets_list[current_idx + 1].focus_set()
        else:
            # If it's the last entry, submit the scores for the round
            self.add_scores_round()

    # This method is no longer used for global Enter binding
    def add_scores_round_event(self, event=None):
        # The logic has been moved to _on_score_entry_return for individual entry binding
        pass

    def add_scores_round(self):
        scores_input = {name: entry.get() for name, entry in self.score_entries.items()}
        game_ended, error_msg = self.game.add_scores_round(scores_input)

        if error_msg:
            messagebox.showerror("Erreur de Saisie", error_msg, parent=self.master)
            return

        if game_ended:
            self.end_game()
        else:
            self.update_game_display()
            # Move focus to the first score entry for the next round
            if self.score_entries:
                list(self.score_entries.values())[0].focus_set()

    def update_game_display(self):
        self.current_round_label.config(text=f"Tour: {self.game._current_round_number}")
        current_scores = self.game.get_current_scores()

        score_display_text = "Scores Actuels: "
        for player_name, total_score in current_scores.items():
            score_display_text += f"{player_name}: {total_score} | "
        self.current_scores_label.config(text=score_display_text.strip(' |'))

        # Clear previous score input fields
        for widget in self.score_input_frame.winfo_children():
            widget.destroy()
        self.score_entries = {}
        self._score_entry_widgets_list = [] # Reset for the new round

        # Display current round's winner and overall leaders
        round_winner_names, round_max_score, round_scores_this_round = self.game.get_round_winner_info()
        if round_winner_names and round_max_score > 0 and self.game._current_round_number > 0:
            self.round_winner_label.config(text=f"Gagnant(s) de la dernière Manche ({self.game._current_round_number}): {', '.join(round_winner_names)} ({round_max_score} points)",
                                           fg=self.HIGHLIGHT_COLOR)
        else:
            self.round_winner_label.config(text="Gagnant de la dernière Manche: Aucun", fg=self.LABEL_TEXT_COLOR)

        overall_leaders, overall_max_score = self.game.get_overall_leader_info()
        if overall_leaders:
            self.overall_leader_label.config(text=f"Leader(s) Général(aux): {', '.join(overall_leaders)} (Total: {overall_max_score})",
                                             fg=self.WINNER_COLOR)
        else:
            self.overall_leader_label.config(text="Leader(s) Général(aux): Aucun", fg=self.LABEL_TEXT_COLOR)

        # Create entries for current round scores
        for i, player_name in enumerate(self.game.players):
            player_frame = tk.Frame(self.score_input_frame, bg=self.FRAME_BG_COLOR)
            player_frame.pack(fill="x", pady=2)
            tk.Label(player_frame, text=f"{player_name} (Total: {current_scores.get(player_name, 0)}):", bg=self.FRAME_BG_COLOR, fg=self.LABEL_TEXT_COLOR, font=(self.FONT_FAMILY, 10)).pack(side=tk.LEFT, padx=5)
            entry = tk.Entry(player_frame, width=10, bg=self.ENTRY_BG_COLOR, fg=self.LABEL_TEXT_COLOR, font=(self.FONT_FAMILY, 10))
            entry.pack(side=tk.LEFT, padx=5)
            self.score_entries[player_name] = entry
            self._score_entry_widgets_list.append(entry) # Add to ordered list
            entry.bind('<Return>', lambda event, current_idx=i: self._on_score_entry_return(event, current_idx)) # Bind Enter key for each score entry
            # Clear the entry for the new round
            entry.delete(0, tk.END)

    def end_game(self):
        self.game_play_frame.pack_forget()
        self.stats_frame.pack(pady=15, padx=15, fill="both", expand=True)
        self.stats_text.delete(1.0, tk.END) # Clear previous text
        self.stats_text.insert(tk.END, self.game.get_stats_report())
        messagebox.showinfo("Partie Terminée", "La partie a atteint le score cible!", parent=self.master)

    def reset_game(self):
        self.stats_frame.pack_forget()
        self.setup_frame.pack(pady=15, padx=15, fill="both", expand=True)
        self.game = Game() # Create a new game instance
        self.player_entries = {}
        self.score_entries = {}
        self._player_entry_widgets_list = [] # Reset this list as well
        self._score_entry_widgets_list = [] # Reset this list as well
        self.target_score_input_var.set("100")
        self.num_players_input_var.set("2")
        for widget in self.player_name_frame.winfo_children():
            widget.destroy()
        # Reset labels
        self.round_winner_label.config(text="Gagnant(s) de la dernière Manche: ", fg=self.LABEL_TEXT_COLOR)
        self.overall_leader_label.config(text="Leader(s) Général(aux): ", fg=self.LABEL_TEXT_COLOR)
        self.current_scores_label.config(text="Scores Actuels: ")
        self.current_round_label.config(text="Tour: 0")

        self.update_start_game_button_state()
        self.add_scores_btn.config(state=tk.DISABLED)
