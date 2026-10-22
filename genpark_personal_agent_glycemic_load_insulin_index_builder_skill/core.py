# -*- coding: utf-8 -*-
"""Glycemic Load & Food Insulin Index Builder for GenPark Personal Agent."""
import json
from typing import Dict, Any, List

class GlycemicLoadInsulinIndexBuilder:
    @staticmethod
    def calculate_meal_glycemic_load_and_insulin_score(ingredients: List[Dict[str, Any]]) -> Dict[str, Any]:
        total_gl = 0.0
        total_carbs = 0.0
        for item in ingredients:
            net_carbs = item.get("net_carbs_g", 0.0)
            gi = item.get("glycemic_index", 50.0)
            gl = (net_carbs * gi) / 100.0
            total_gl += gl
            total_carbs += net_carbs
            
        total_gl = round(total_gl, 1)
        if total_gl <= 10.0:
            category = "LOW_GL_MINIMAL_INSULIN_DEMAND"
        elif total_gl <= 19.0:
            category = "MODERATE_GL_ACCEPTABLE"
        else:
            category = "HIGH_GL_INSULIN_SPIKE_RISK"
            
        return {
            "total_net_carbs_g": round(total_carbs, 1),
            "aggregate_meal_glycemic_load": total_gl,
            "metabolic_classification": category,
            "estimated_postprandial_insulin_demand": "High Beta-Cell Secretion" if total_gl > 19 else "Basal Physiological Steady State"
        }

    @staticmethod
    def prescribe_low_insulinemic_food_pairings(baseline_meal_gl: float) -> Dict[str, Any]:
        modifiers = [
            "Add 15ml Extra Virgin Olive Oil or 1/2 avocado to slow gastric emptying rate",
            "Consume 10g viscous soluble fiber (psyllium husk or chia seeds) 15 min prior to meal",
            "Incorporate 1 tablespoon apple cider vinegar or lemon juice to inhibit salivary and pancreatic alpha-amylase"
        ]
        return {
            "original_glycemic_load": baseline_meal_gl,
            "expected_gl_reduction_pct": 28.0,
            "recommended_meal_attenuators": modifiers
        }
