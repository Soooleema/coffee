# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: MoneyMinder
import sys

def main():
    parser = argparse.ArgumentParser(description="MoneyMinder: личный финансовый журнал")
    sub = parser.add_subparsers(dest="command")
    income = sub.add_parser("income", help="записать доход")
    income.add_argument("--amount", type=float, required=True)
    income.add_argument("--category", default="other")
    income.add_argument("--date", default=None)
    expense = sub.add_parser("expense", help="записать расход")
    expense.add_argument("--amount", type=float, required=True)
    expense.add_argument("--category", default="other")
    expense.add_argument("--date", default=None)
    goals = sub.add_parser("goal", help="создать цель")
    goals.add_argument("--name", required=True)
    goals.add_argument("--target", type=float, required=True)
    goals.add_argument("--date", default=None)
    reports = sub.add_parser("report", help="отчёт")
    reports.add_argument("--period", default="month")
    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        return
    data = load_data()
    if args.command == "income":
        data["income"].append({"amount": args.amount, "category": args.category, "date": args.date or now()})
    elif args.command == "expense":
        data["expense"].append({"amount": args.amount, "category": args.category, "date": args.date or now()})
    elif args.command == "goal":
        data["goals"].append({"name": args.name, "target": args.target, "date": args.date or now()})
    elif args.command == "report":
        print_report(data, args.period)
    save_data(data)

if __name__ == "__main__":
    main()
