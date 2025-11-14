#!/usr/bin/env python3
"""
Progression tracking system for PSE learning.
Manages student progress through the roadmap tiers, subtiers, and concepts.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


class ProgressionManager:
    """Manages student progression through PSE roadmap."""
    
    def __init__(self, filepath: str = "progression.json"):
        self.filepath = Path(filepath)
        self.data = self._load_or_create()
    
    def _load_or_create(self) -> Dict:
        """Load existing progression or create new one."""
        if self.filepath.exists():
            with open(self.filepath, 'r') as f:
                return json.load(f)
        else:
            return self._create_new_progression()
    
    def _create_new_progression(self) -> Dict:
        """Create new progression structure based on roadmap."""
        return {
            "student_info": {
                "started": datetime.now().isoformat(),
                "last_session": datetime.now().isoformat(),
                "total_sessions": 0
            },
            "current_position": {
                "tier": 1,
                "subtier": "1.1",
                "concept": "Calculus",
                "subconcept": "Single and multivariable calculus"
            },
            "completed": {
                "concepts": [],
                "subtiers": [],
                "tiers": []
            },
            "mastery_status": {},
            "spaced_repetition": {
                "due_for_review": [],
                "review_history": []
            },
            "exercises_completed": [],
            "cheat_sheets_generated": [],
            "problem_sets_completed": []
        }
    
    def save(self):
        """Save progression to file."""
        self.data["student_info"]["last_session"] = datetime.now().isoformat()
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def complete_subconcept(self, concept: str, subconcept: str):
        """Mark a subconcept as completed."""
        entry = f"{concept} > {subconcept}"
        if entry not in self.data["completed"]["concepts"]:
            self.data["completed"]["concepts"].append(entry)
    
    def complete_concept(self, subtier: str, concept: str):
        """Mark a concept as fully completed."""
        entry = f"{subtier} > {concept}"
        if entry not in self.data["completed"]["concepts"]:
            self.data["completed"]["concepts"].append(entry)
    
    def complete_subtier(self, subtier: str):
        """Mark a subtier as completed."""
        if subtier not in self.data["completed"]["subtiers"]:
            self.data["completed"]["subtiers"].append(subtier)
    
    def complete_tier(self, tier: int):
        """Mark a tier as completed."""
        if tier not in self.data["completed"]["tiers"]:
            self.data["completed"]["tiers"].append(tier)
    
    def update_position(self, tier: int, subtier: str, concept: str, subconcept: str):
        """Update current learning position."""
        self.data["current_position"] = {
            "tier": tier,
            "subtier": subtier,
            "concept": concept,
            "subconcept": subconcept
        }
    
    def add_exercise_completion(self, concept: str, subconcept: str, exercises_count: int):
        """Record exercise completion."""
        self.data["exercises_completed"].append({
            "concept": concept,
            "subconcept": subconcept,
            "count": exercises_count,
            "timestamp": datetime.now().isoformat()
        })
    
    def add_cheat_sheet(self, subtier: str, concept: str):
        """Record cheat sheet generation."""
        entry = f"{subtier} > {concept}"
        if entry not in self.data["cheat_sheets_generated"]:
            self.data["cheat_sheets_generated"].append(entry)
    
    def add_problem_set(self, subtier: str):
        """Record problem set completion."""
        if subtier not in self.data["problem_sets_completed"]:
            self.data["problem_sets_completed"].append(subtier)
    
    def add_to_review_queue(self, concept: str, days_until_review: int = 7):
        """Add concept to spaced repetition queue."""
        review_date = datetime.now()
        # Add days to review date
        self.data["spaced_repetition"]["due_for_review"].append({
            "concept": concept,
            "due_date": review_date.isoformat(),
            "days_until_review": days_until_review
        })
    
    def get_due_reviews(self) -> List[str]:
        """Get concepts due for review."""
        now = datetime.now()
        due = []
        for item in self.data["spaced_repetition"]["due_for_review"]:
            due_date = datetime.fromisoformat(item["due_date"])
            if due_date <= now:
                due.append(item["concept"])
        return due
    
    def increment_session(self):
        """Increment session counter."""
        self.data["student_info"]["total_sessions"] += 1
    
    def get_summary(self) -> str:
        """Generate progression summary."""
        current = self.data["current_position"]
        completed = self.data["completed"]
        
        summary = f"""
=== PSE Learning Progression Summary ===

Current Position:
  Tier {current['tier']}: {current['subtier']} - {current['concept']}
  Subconcept: {current['subconcept']}

Progress Statistics:
  Total Sessions: {self.data['student_info']['total_sessions']}
  Concepts Completed: {len(completed['concepts'])}
  Subtiers Completed: {len(completed['subtiers'])}
  Tiers Completed: {len(completed['tiers'])}
  Cheat Sheets: {len(self.data['cheat_sheets_generated'])}
  Problem Sets: {len(self.data['problem_sets_completed'])}

Spaced Repetition:
  Items Due for Review: {len(self.get_due_reviews())}
"""
        return summary


def initialize_progression(output_path: str = "progression.json") -> str:
    """Initialize new progression file."""
    manager = ProgressionManager(output_path)
    manager.save()
    return f"Initialized progression file at {output_path}"


def load_progression(filepath: str = "progression.json") -> ProgressionManager:
    """Load existing progression file."""
    return ProgressionManager(filepath)


if __name__ == "__main__":
    # Example usage
    manager = ProgressionManager("progression.json")
    print(manager.get_summary())
    manager.save()
