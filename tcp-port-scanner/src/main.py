import argparse
import sys
from utils.validators import validators
from utils.logger import logger
from scanner.tcp_scanner import Scanner
from output.terminal import terminal
from output.report import report


def parse_ports(ports_str):
	"""Parse a ports argument like "22,80,443" or "20-25" into a list of ints."""
	ports = set()
	for part in ports_str.split(','):
		part = part.strip()
		if not part:
			continue
		if '-' in part:
			start, end = part.split('-', 1)
			start = int(start)
			end = int(end)
			ports.update(range(start, end + 1))
		else:
			ports.add(int(part))
	return sorted(p for p in ports if validators.validate_port(p))


def main(argv=None):
	argv = argv if argv is not None else sys.argv[1:]
	parser = argparse.ArgumentParser(description='Simple TCP port scanner')
	parser.add_argument('ip', help='Target IP address to scan')
	parser.add_argument('-p', '--ports', default='1-1024',
						help='Comma-separated ports or ranges (e.g. 22,80,1000-1010). Default: 1-1024')
	parser.add_argument('-r', '--report', action='store_true', help='Generate a textual report')
	parser.add_argument('-l', '--log', default='scanner.log', help='Log file path')
	args = parser.parse_args(argv)

	if not validators.validate_ip(args.ip):
		print(f"Invalid IP address: {args.ip}")
		return 2

	try:
		ports = parse_ports(args.ports)
	except ValueError:
		print(f"Invalid ports specification: {args.ports}")
		return 2

	if not ports:
		print("No valid ports to scan after parsing/validation.")
		return 2

	log = logger(args.log)
	log.log(f"Starting scan: {args.ip} ports={len(ports)}")

	scanner = Scanner(args.ip, ports)

	try:
		open_ports = scanner.scan_ports()
	except KeyboardInterrupt:
		print("Scan cancelled by user")
		log.log("Scan cancelled by user")
		return 130

	log.log(f"Scan complete: found {len(open_ports)} open ports")

	# Output results
	term = terminal(open_ports)
	term.display_open_ports()

	if args.report:
		rep = report(open_ports)
		content = rep.generate_report()
		out_path = 'open_ports_report.txt'
		with open(out_path, 'w') as f:
			f.write(content)
		print(f"Report written to {out_path}")
		log.log(f"Report written to {out_path}")

	return 0


if __name__ == '__main__':
	raise SystemExit(main())

