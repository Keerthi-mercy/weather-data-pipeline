# How to Run the Weather Pipeline (Quick Steps)

Follow these steps every time you want to run the project again.

## Step 1: Open PyCharm
Open your `weather-pipeline` project.

## Step 2: Start the pipeline (keep it running)
1. Open a Terminal tab
2. Type:
   ```
   python save_to_db.py
   ```
3. Wait until you see:
   ```
   Your flow 'weather-pipeline-flow' is being served and polling for scheduled runs!
   ```
4. **Leave this terminal open** — don't close it, don't close PyCharm.
   This is your "engine" running in the background. It fetches new
   weather data automatically every hour, as long as this terminal
   stays open.

## Step 3 (optional): Get data faster instead of waiting an hour
1. Open a **second** terminal tab (click the "+" near the terminal tabs)
2. Type:
   ```
   prefect deployment run 'weather-pipeline-flow/weather-pipeline-deployment'
   ```
3. Repeat this every few minutes if you want more data points quickly
   (useful before a demo or interview, so your dashboard chart has
   more points to show)

## Step 4: View your dashboard
1. Open a **third** terminal tab
2. Type:
   ```
   streamlit run dashboard.py
   ```
3. It should open automatically in your browser, or visit:
   ```
   http://localhost:8501
   ```

## Step 5: Check the data directly in MySQL (optional)
1. Open MySQL Workbench
2. Run:
   ```sql
   SELECT * FROM weather_pipeline.weather_readings;
   ```

## Step 6: When you're done for the day
Just close PyCharm normally — nothing special to shut down.
Next time you want fresh data, just repeat Step 2.

---

## Troubleshooting

**"My dashboard isn't showing new data"**
→ Check that the terminal from Step 2 is still open and shows
"being served and polling for scheduled runs." If that terminal
got closed (PyCharm closed, laptop slept, etc.), the automation
stops completely — just restart it with `python save_to_db.py`.

**"Streamlit shows a 'missing ScriptRunContext' warning"**
→ You ran `dashboard.py` with the green ▶️ Run button instead of
the terminal command. Always use `streamlit run dashboard.py`
in the terminal instead.

**"I forgot my API key or MySQL password"**
→ They're saved safely in your `.env` file in the project folder
(never uploaded to GitHub, thanks to `.gitignore`).
