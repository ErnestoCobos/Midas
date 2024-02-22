# Midas 
![Logo of the Midas, created in Procreate](assets%2Flogo.png)
Midas is a service designed to assist with daily trading on the Bitso platform. The idea for Midas was born out of a need for an extra income and the challenge of keeping up with the constant changes in the markets. 

The main issue was the difficulty in remembering to check the markets or simply not having the time to do so. This led to the idea of creating a bot that could handle this task. The bot is designed to take a snapshot of the market every 20 minutes, allowing for a constant update on the state of the markets. This approach helps to minimize losses and maximize gains.

The primary focus is on monitoring the efficiency parameter, which is a percentage of how much the bot is expected to earn based on the initial amount. Over time, the goal is to refine this parameter to reflect monthly and then yearly gains.

## Indicators for Day Trading

In day trading, traders use a variety of technical indicators to analyze the market and make informed decisions. These indicators can help identify trends, entry and exit points, and buy or sell signals. Here are some of the most common and necessary indicators in day trading:

1. **Moving Averages (MA)**
   - Simple Moving Average (SMA) and Exponential Moving Average (EMA): Moving averages help to smooth out price action to identify the trend. The EMA gives more weight to the most recent data and reacts faster to price changes than the SMA.
2. **Relative Strength Index (RSI)**
   - Description: The RSI is a momentum oscillator that measures the speed and change of price movements. Values typically oscillate between 0 and 100, with levels marked at 30 (oversold) and 70 (overbought) to indicate possible reversal points.
3. **Bollinger Bands**
   - Description: This indicator consists of an SMA (usually 20 days) as the center line, with two outer bands that adjust according to market volatility (usually two standard deviations above and below the SMA). The bands widen during periods of higher volatility and contract during periods of lower volatility, helping to identify market volatility and possible breakout points.
4. **MACD (Moving Average Convergence Divergence)**
   - Description: The MACD measures the relationship between two EMAs (for example, 12 and 26 days). A positive MACD indicates that the 12-day EMA is above the 26-day EMA, signaling bullish momentum, while a negative MACD suggests the opposite. The signal line (an EMA of the MACD, typically 9 days) can generate buy or sell signals when the MACD crosses it.
5. **Volume**
   - Description: Trading volume is crucial for confirming trends and signals. A price movement accompanied by high volume is more likely to indicate a sustainable trend than a price movement with low volume.
6. **VWAP (Volume Weighted Average Price)**
   - Description: The VWAP gives the average price of an asset weighted by volume over a period of time, usually a trading day. It is useful for identifying support and resistance areas and for traders looking to compare the current price with the day's average.
7. **Fibonacci Retracement**
   - Description: This technical indicator uses horizontal lines to indicate support or resistance areas at key Fibonacci levels (23.6%, 38.2%, 50%, 61.8% and 100%) based on maximum and minimum price movements. It is popular for identifying possible price reversal points.

### How to Use Them

- **Combination of Indicators**: Day traders often combine several indicators to confirm signals and improve the accuracy of their predictions. For example, a trader might use RSI and MACD to identify market strength, while using Bollinger Bands and the VWAP to identify potential entry and exit points.
- **Market Context Analysis**: In addition to technical indicators, it is crucial to consider the broader market context, including economic news, geopolitical events, and developments within specific sectors or companies.

## Market Context Analysis

Market context analysis goes beyond technical indicators and focuses on understanding the macroeconomic, political, and sectoral environment that can affect asset prices. Although not "indicators" in the technical sense, there are several factors and analysis tools that investors and traders use to make informed decisions. Here are some of the most relevant:

1. **Fundamental Analysis**
   - Economic Data: Reports on GDP, interest rates, employment, inflation, and trade balance can significantly influence financial markets.
   - Corporate Results: Earnings, revenue, debt, and other financial indicators of specific companies are crucial for stock investors.
   - Sector Health: The performance of specific sectors (technology, consumer goods, energy, etc.) can indicate broader economic trends.
2. **Market Sentiment**
   - Sentiment Surveys: Tools like the Fear and Greed Index, consumer and investor confidence surveys can give an idea of the general market sentiment.
   - Social Media and News Analysis: Monitoring trends on social media and news can provide early signals about changes in market perception towards certain assets or sectors.
3. **Geopolitical Events**
   - Conflicts and Political Tensions: Events such as wars, elections, trade disputes, and sanctions can have significant impacts on markets.
   - Monetary and Fiscal Policies: Decisions by central banks (for example, changes in interest rates, open market operations) and government policies (fiscal stimuli, regulations) are key determinants of the investment environment.
4. **Market Indicators**
   - Volatility Indices: The VIX (often called the "fear index") measures the expected volatility of the stock market and is a key indicator of market sentiment.
   - Capital Flows: Movements of capital towards or away from certain types of assets (stocks, bonds, commodities) can indicate changes in investors' risk preference.
5. **Technical Analysis of Context**
   - Support and Resistance Levels: Although technical, these levels can be influenced by external factors and offer insights into market psychology.
   - Chart Patterns: Patterns like "head and shoulders", "double tops", and "flags" can indicate potential changes in the trend that, although based on technical analysis, should be considered in the broader market context.

### How to Use Them to Make Decisions

- **Combination of Analysis**: The most successful traders and investors combine market context analysis with technical indicators to form a complete view before making decisions.
- **Adaptability**: The market context is constantly changing, so it is crucial to stay informed and be able to adapt investment and trading strategies as the environment evolves.
- **Risk Management**: Regardless of the indicators or analysis used, effective risk management is essential to protect against volatility and unexpected market movements.

Understanding the market context requires a holistic view and the ability to interpret how global events, economic trends, and political changes can affect financial markets.

## TODO
- [ ] Implement the bot to monitor the markets every 20 minutes.
- [ ] Develop the efficiency parameter to calculate expected earnings.
- [ ] Refine the efficiency parameter to reflect monthly and then yearly gains.
- [ ] Implement error handling and exception management.
- [ ] Improve documentation and code comments.
- [ ] Implement unit tests for all functions and methods.
- [ ] Optimize the performance of the bot.
- [ ] Implement all types of indicators:
    - [X] Moving Averages (MA)
    - [X] Relative Strength Index (RSI)
    - [X] Bollinger Bands
    - [X] MACD (Moving Average Convergence Divergence)
    - [X] Volume
    - [X] VWAP (Volume Weighted Average Price)
    - [X] Fibonacci Retracement
- [ ] Implement Market Context Analysis indicators:
    - [ ] Fundamental Analysis
    - [ ] Market Sentiment
    - [ ] Geopolitical Events
    - [ ] Market Indicators
    - [ ] Technical Analysis of Context
- [ ] Implement a combination of indicators and analysis to make informed decisions.
- [ ] Implement adaptability and risk management strategies.
- [ ] Implement a user interface for the bot.
- [ ] Implement a database to store market data and user preferences.
- [ ] Implement a notification system for alerts and updates.
- [ ] Implement a web scraping module to gather news and social media data.
- [ ] Implement a machine learning module for predictive analysis.
- [ ] Implement a backtesting module to evaluate the performance of the bot.
- [ ] Implement a paper trading module for simulated trading.
- [ ] Implement a live trading module for real-time trading.
- [ ] Implement a portfolio management module for asset allocation and diversification.
- [ ] Implement a reporting module for performance analysis and visualization.

--- 
- [ ] Implement a community module for user interaction and collaboration.
- [ ] Implement a subscription module for premium features and services.
- [ ] Implement a security module for data protection and privacy.
- [ ] Implement a compliance module for regulatory requirements.
- [ ] Implement a support module for user assistance and issue resolution.
- [ ] Implement a feedback module for user suggestions and feature requests.
- [ ] Implement a marketing module for promotion and user acquisition.
- [ ] Implement a monetization module for revenue generation.
- [ ] Implement a legal module for terms of service and privacy policy.
- [ ] Implement a business model for sustainability and growth.
- [ ] Implement a roadmap for future development and expansion.
- [ ] Implement a team and organization for project management and collaboration.
- [ ] Implement a governance model for decision-making and accountability.
- [ ] Implement a code of conduct for ethical and responsible behavior.
- [ ] Implement a community engagement strategy for user involvement.
- [ ] Implement a branding and design strategy for user experience.
- [ ] Implement a communication strategy for outreach and engagement.
- [ ] Implement a partnership strategy for collaboration and growth.
- [ ] Implement a funding strategy for investment and financial sustainability.

**Note**: Some of the task of the todo list are just ideas and may not be implemented. I write this at 3AM and I'm tired.
