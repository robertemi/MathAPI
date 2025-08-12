def generate_report(data: dict):
    report = []

    for key, value in data.items():
        if value > 80:
            report.append((key, value))

    return sorted(report, key=lambda pair: pair[1], reverse=True)