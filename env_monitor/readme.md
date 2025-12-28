                 ┌───────────────────────┐
                 │   External APIs       │
                 │ (Air & Water Quality) │
                 └─────────┬────────────┘
                           │ fetch data
                           ▼
                 ┌───────────────────────┐
                 │      Django App       │
                 │       monitor         │
                 ├──────────┬────────────┤
                 │ Models   │ AirQuality  │
                 │          │ WaterQuality│
                 ├──────────┴────────────┤
                 │ Views / REST API       │
                 │ - Dashboard            │
                 │ - API Endpoints        │
                 ├──────────┬────────────┤
                 │ Utils    │ Alerts      │
                 │          │ Email/SMS   │
                 └──────────┴────────────┘
                           │ store/retrieve
                           ▼
                 ┌───────────────────────┐
                 │       MySQL DB        │
                 │  (Air & Water Data)  │
                 └─────────┬────────────┘
                           │ display
                           ▼
                 ┌───────────────────────┐
                 │   Dashboard (UI)      │
                 │ - Chart.js graphs     │
                 │ - Historical trends   │
                 └───────────────────────┘
