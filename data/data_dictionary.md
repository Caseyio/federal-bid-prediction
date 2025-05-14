## Data Dictionary: Cleaned Health IT Contract Awards

| Variable              | Type      | Description                                                                 |
|-----------------------|-----------|-----------------------------------------------------------------------------|
| `award_id`            | string    | Unique identifier for the federal contract award                           |
| `recipient`           | string    | Name of the vendor or organization receiving the award                     |
| `agency`              | string    | Federal agency awarding the contract (e.g., HHS, VA)                       |
| `naics_code`          | string    | 6-digit NAICS industry classification code (e.g., 541512 = Custom Software)|
| `naics_description`   | string    | Description of the NAICS code                                               |
| `award_amount`        | numeric   | Total dollar value awarded to the vendor (target variable, log-transformed in model) |
| `offers_received`     | integer   | Number of bids or offers submitted for the contract                        |
| `set_aside`           | string    | Special designation (e.g., 8A, SDVOSB, HUBZone) limiting eligible bidders   |
| `pricing_type`        | string    | Type of contract pricing (e.g., Firm Fixed Price, Cost Plus Award Fee)     |
| `state`               | string    | Two-letter code for place of performance (e.g., MD, VA)                    |
| `start_date`          | date      | Contract period start date                                                 |
| `end_date`            | date      | Contract period end date                                                   |
