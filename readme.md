# raffle.py

Inputs:

1. path to entries JSON 
2. path to stock JSON
3. optional: integer value for an item limit

Example usage: `raffle.py entries.json stock.json 2`

Example output: `results.json`
```javascript
{
    "remaining stock": {
        "Ecto: Topre": 6
    },
    "winners": [
        {
            "RoastPotatoes": [
                "Ecto: Topre",
                "Callisto: MX"
            ]
        },
        {
            "Deductivemonkee": [
                "Pulsate: Topre"
            ]
        },
        {
            "nathanrosspowell": [
                "Ecto: Topre",
                "Pulsate: Topre"
            ]
        },
        {
            "deduction": [
                "Ecto: Topre"
            ]
        },
        {
            "Hispes": [
                "Ecto: Topre"
            ]
        }
    ]
}
```
