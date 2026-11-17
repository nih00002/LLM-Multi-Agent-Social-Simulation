# LLM Multi-Agent Social Simulation

**Personality-conditioned, LLM-based experiments on cooperation, negotiation, and collaboration.**

This Python project generates synthetic scientist personas and simulates their interactions using language-model agents. It compares three ways of conditioning an agent's behavior: a life story, a Big Five personality profile, or both. The experiments study how these representations relate to decisions and group outcomes in three controlled social scenarios. Analysis tools produce tables, regression summaries, and figures from the simulated traces.

> **Project status:** Source code and configuration are included. The provided archive contained no completed simulation outputs, measured findings, or reproducible experimental run logs. Running the complete pipeline requires access to an LLM provider and may incur API charges. Do not interpret simulated behaviors as observed human behavior.

## What the project explores

| Dimension | Included configurations |
|---|---|
| Persona input | Synthetic biographies and LLM-scored Big Five inventory items |
| Prompt conditions | `life_story_only`, `bfi_only`, `life_story_and_bfi` |
| Social scenarios | Public-goods contributions, resource negotiation, collaborative research planning |
| Agent capabilities | LLM decisions, structured action output, lightweight TF-IDF event memory |
| Analysis | Action and reward metrics, LLM judging, regressions, uncertainty summaries, action clustering |

### Experiment pipeline

```text
data/surveys.json
       |
       v
Generate synthetic personas ----> data/population.json
       |
       v
Simulate three scenarios × three prompt conditions
       |
       v
outputs/results/simulation_manifest.json + interaction traces
       |
       v
Analyze outcomes, calibrate judged metrics, cluster behaviors
       |
       v
outputs/results/{summary.json, tables/, plots/, reports/}
```

## Quick start

Requires **Python 3.11 or 3.12** and an API key for the configured LLM provider.

```bash
# From the repository root
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt
```

For the default model (`gemini/gemini-3-flash-preview` in `conf/`), copy `.env.example` to `.env`, then supply your own authorized `GEMINI_API_KEY`. **Never commit `.env`.** The entry scripts read `.env` via `python-dotenv`; you can also set environment variables outside the project. Provider/model availability can change, so adjust the model names in the YAML configuration if needed.

Use these commands in sequence:

```bash
python generate_population.py
python run_experiments.py
python run_analysis.py
```

Default settings in `conf/` request 100 personas, four agents per group, and three prompt conditions. **Generating personas and running the simulations make many LLM calls.** Review the model choice, concurrency limits, and expected API costs before running the default configuration.

For a smaller *simulation stage* after generating a population:

```bash
python run_experiments.py simulation.max_groups=3 output.base_dir=outputs/test_run
python run_analysis.py output.base_dir=outputs/test_run
```

Note that this overrides the number of simulation groups, not the 100-persona generation cost. To reduce persona generation, use `python generate_population.py population.n=8 population.max_parallel_bio_workers=2`; the output is then a new smaller population rather than a subset of an existing one.

## Configuration

| File | Purpose |
|---|---|
| `conf/population/default.yaml` | Persona count, seed, biography generation model |
| `conf/agent/llm.yaml` | Simulation model and sampling temperature |
| `conf/simulation/default.yaml` | Scenarios, group sizes, rounds, context conditions, concurrency |
| `conf/analysis/default.yaml` | LLM judge, confidence intervals, embedding and clustering parameters |
| `conf/calibration/default.yaml` | **Hypothetical**, not empirically measured, judge calibration parameters |
| `conf/output/default.yaml` | Output root (`outputs/results`) |

The personality inventory in `data/surveys.json` was included in the source archive and described there as supplied within an assignment context. The generated Big Five responses are *model outputs*, not responses from human study participants. Likewise, any adjusted judged rates depend on assumed sensitivity and specificity values; the calibration file is explicitly **pedagogical**, not an independent validation study.

## Repository layout

```text
agents/                LLM agent and base agent
core/                  Local TF-IDF interaction memory
envs/                  Public goods, negotiation, collaboration
eval/                  Metrics and calibration helpers
utils/                 IO and async parallel utilities
conf/                  Hydra configuration groups
data/surveys.json       Personality inventory schema
generate_population.py  Persona generation
run_experiments.py      LLM interaction simulations
run_analysis.py         Analysis and visualization
requirements.txt       Direct application dependencies
.env.example           API key placeholder (safe to commit)
.gitignore             Excludes secrets, local caches and generated data
tests/                 Offline unit tests
```

The full package snapshot from the supplied archive is kept in `docs/requirements-original-snapshot.txt` for traceability. That snapshot contains transitive and platform-specific dependencies; `requirements.txt` is the cleaner application dependency list.

## Offline verification

Run lightweight tests **without making any model API calls**:

```bash
python -m unittest discover -s tests -v
python -m compileall -q agents core envs eval utils generate_population.py run_experiments.py run_analysis.py
```

These checks validate a few deterministic components and Python syntax only. They are not substitutes for a full end-to-end simulation and analysis run.

## Limitations and responsible use

- Simulated agents are **not human participants**, and Big Five scores are generated or inferred by model prompts.
- LLM outputs, API availability, model versions, and randomness can change the outcomes.
- The LLM judge is not a human rater; calibration parameters in this repository are hypothetical.
- Clustering and t-SNE visualizations are exploratory; do not interpret them as externally validated social types.
- Do not upload API credentials, confidential prompts, identifiable personal data or provider logs to a public repository.

## Repository

GitHub: <https://github.com/nih00002/LLM-Multi-Agent-Social-Simulation>

**Source provenance:** This is a cleaned and documented GitHub presentation of the social-simulation source archive supplied for this project. The archive did not establish a software license or original authorship. Before public redistribution, confirm you have permission to publish the source and survey items. No benchmark results or personal authorship claims were invented during packaging.
