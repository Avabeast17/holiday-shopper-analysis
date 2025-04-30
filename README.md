# Hey there! I'm Caprice

# Holiday Shopper Behavior Analysis

This project analyzes online customer behavior during the peak shopping months of November and December.

## Key Questions Answered
- What are the purchase rates for returning vs. new customers?
- Which customer page behaviors are most correlated?
- What’s the probability of campaign success based on boosted purchase rates?

## Results
- **Purchase Rates**:
  - Returning Customers: 19.6%
  - New Customers: 27.3%
- **Top Correlation**: Admin Duration ↔ Product Duration (0.417)
- **Campaign Model**: 92.27% chance of 100+ purchases (with 15% rate increase)

## Files
- `holiday_shopper_analysis.py`: Full analysis with code comments and visuals

## Tech Stack
`Python` `pandas` `scipy.stats` `matplotlib`

## How to Run
```bash
pip install pandas matplotlib scipy
python holiday_shopper_analysis.py
