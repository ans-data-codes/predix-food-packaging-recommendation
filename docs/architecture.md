# PREDIX Architecture

## End-to-End Flow

User Input -> Data Validation -> Property Analysis -> Requirement Derivation -> Compatibility and Candidate Filtering -> Hybrid Intelligence (Rule Layer + ML Ranking) -> Multi-Criteria Scoring -> Shelf-Life/Performance Analysis -> Cost and Sustainability Analysis -> Explainability -> Final Recommendation

## Major Modules

- `src/schemas`: Typed domain schemas and result contracts.
- `src/data`: Input loading, validation, normalization, and preparation.
- `src/requirements`: Property analysis and packaging requirement derivation.
- `src/knowledge`: Domain rule interfaces, compatibility checks, MAP/fresh-produce guideline interfaces, and source metadata retrieval.
- `src/packaging_db`: Packaging material repository and candidate filtering.
- `src/ranking`: Configurable weighted scoring and ranking interfaces.
- `src/models`: Future ML training, prediction, and evaluation interfaces.
- `src/shelf_life`: Shelf-life estimation interface placeholders.
- `src/sustainability`: Recyclability/biodegradability and sustainability scoring interfaces.
- `src/explainability`: Transparent explanation and warning generation.
- `src/recommendation`: Pipeline orchestration entry point.

## Design Principles

1. Rule layer governs feasibility and compatibility.
2. ML layer ranks only feasible candidates.
3. OTR/WVTR are represented with test-condition context.
4. Confidence is separate from suitability.
5. Recommendations remain decision-support outputs requiring expert validation.
