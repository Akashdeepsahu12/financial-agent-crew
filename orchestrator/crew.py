
from agents.researcher import research_task
from agents.analyst import analysis_task
from agents.writer import write_report

from tools.market_data import get_stock_data
from tools.sentiment import get_news
from tools.charting import generate_chart

from utils.logger import AgentLogger

def run_crew(company, ticker):
    logger = AgentLogger()

    tools = {
        "market": get_stock_data,
        "news": get_news,
        "chart": generate_chart
    }

    logger.log("System", "Starting AI Crew")

    research = research_task(company, tools, logger)
    analysis = analysis_task(ticker, tools, logger)
    report = write_report(company, research, analysis, logger)

    logger.log("System", "Finished AI Crew")

    logger.save()
    return report, logger.get_logs()
