
def write_report(company, research, analysis, logger):
    logger.log("Writer", "Writing report")

    report = f'''
Financial Report: {company}

=== Market News ===
{research}

=== Stock Analysis ===
{analysis['summary']}

Chart Path: {analysis['chart']}

=== Recommendation ===
This is an automated analysis. Consider further financial review before investing.
'''

    logger.log("Writer", "Report completed")
    return report
