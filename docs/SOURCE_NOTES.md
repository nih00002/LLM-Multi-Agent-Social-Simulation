# Source and packaging notes

The user supplied `agents-pset-2-code.zip`, containing a social simulation project titled “Problem Set 2: Social Simulation Experiments.” This GitHub-ready package retains the substantive implementation and original configuration semantics while giving it a descriptive public-facing repository name.

Changes for publication:

- Renamed the project and replaced the assignment-oriented README with task-specific documentation.
- Added `.gitignore`, `.env.example`, and optional environment-variable loading to entry scripts.
- Replaced a full environment freeze in the root with a direct-dependency `requirements.txt`; archived the original list for reference.
- Prepared Matplotlib's noninteractive backend and writable configuration path before loading `pyplot` in `run_analysis.py`.
- Added offline unit tests and Python syntax checks.

No model API run or empirical evaluation has been executed as part of this packaging. The calibration values in `conf/calibration/default.yaml` are explicitly hypothetical, as disclosed by the original code.

The supplied archive included no LICENSE. Verify legal permission to share the code and the survey item wording before publishing to a public repository. These changes do not establish authorship of original code.
