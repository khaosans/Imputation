Contributing to AAVAIL Imputation Project
==========================================

Thank you for your interest in contributing to this project! This document provides guidelines and instructions for contributing.

## Development Workflow

### 1. Branching Strategy

- **Main branch**: Contains production-ready code
- **Feature branches**: Create branches for new features or improvements
  ```bash
  git checkout -b feature/your-feature-name
  ```

### 2. Code Standards

- Follow PEP 8 style guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep notebooks clean and well-documented

### 3. Notebook Guidelines

Before committing notebooks:

1. **Clear outputs** to reduce file size and avoid merge conflicts:
   ```bash
   jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace notebooks/*.ipynb
   ```

2. **Ensure reproducibility**:
   - All cells should execute in order without errors
   - Include clear markdown explanations
   - Document data sources and assumptions

3. **Visualization standards**:
   - All plots must have titles, axis labels, and legends
   - Use consistent color palettes
   - Save visualizations to `reports/assets/` directory

### 4. Documentation

- Update `README.md` if you add new features or change the project structure
- Update `docs/DATA_DICTIONARY.md` if you modify data schemas
- Add citations to `docs/REFERENCES.md` for new external sources
- Follow APA citation style for academic references

### 5. Testing

- Test notebooks in a clean environment before committing
- Verify that all visualizations generate correctly
- Ensure processed data outputs are valid

### 6. Commit Messages

Use clear, descriptive commit messages following conventional commits:

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `refactor:` for code refactoring
- `style:` for formatting changes
- `test:` for adding tests

Example:
```
feat: Add market comparison visualization
docs: Update README with new notebook information
fix: Correct imputation logic for subscriber_type
```

### 7. Pull Request Process

1. Ensure your branch is up to date with `main`
2. Create a pull request with a clear description
3. Reference any related issues
4. Request review from team members
5. Address feedback before merging

## Data Governance

- **Never commit sensitive data** - Use `.gitignore` to exclude sensitive files
- **Raw data is immutable** - Only modify data in `data/processed/`
- **Document all transformations** - Explain imputation strategies and data cleaning steps

## Questions?

If you have questions about contributing, please:
1. Check existing documentation in `docs/`
2. Review the project plan in `docs/PROJECT_PLAN.md`
3. Open an issue for discussion

Thank you for contributing!

