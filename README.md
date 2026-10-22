# Glycemic Load & Food Insulin Index (FII) Meal Builder Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

Glycemic index (GI) vs Glycemic load (GL) computation, Food Insulin Index (FII) food pairing, and postprandial insulin AUC minimizer. Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `calculate_meal_glycemic_load_and_insulin_score`: Calculate total meal Glycemic Load (GL) and Food Insulin Demand score from component ingredients.
- `prescribe_low_insulinemic_food_pairings`: Synthesize fiber, healthy lipid, and acid modifiers to blunt postprandial insulin surge.

## 🚀 Installation & Usage
```bash
python -m genpark_personal_agent_glycemic_load_insulin_index_builder_skill.server --test
```
