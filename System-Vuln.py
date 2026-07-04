def ask_yes_no(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer in ["yes", "no"]:
            return answer
        print("Please enter yes or no.")


score = 0
findings = []
recommendations = []

print("=== System Vulnerability Checklist ===")

# Step 1: Identity Front Door
weak_password = ask_yes_no("Do you use a weak or short password on your main account?")
if weak_password == "yes":
    score += 2
    findings.append("Weak or short password detected.")
    recommendations.append("Use a long passphrase instead of a short simple password.")

weak_mfa = ask_yes_no("Do you rely only on SMS or no MFA at all?")
if weak_mfa == "yes":
    score += 2
    findings.append("Weak or missing MFA detected.")
    recommendations.append("Use stronger MFA such as an authenticator app or passkeys.")

# Step 2: Software Decay
updates_off = ask_yes_no("Are automatic operating system updates disabled?")
if updates_off == "yes":
    score += 2
    findings.append("Automatic OS updates are disabled.")
    recommendations.append("Enable automatic system updates.")

browser_old = ask_yes_no("Is your browser outdated?")
if browser_old == "yes":
    score += 1
    findings.append("Browser is not fully updated.")
    recommendations.append("Update the browser to the latest version.")

av_old = ask_yes_no("Is antivirus missing or outdated?")
if av_old == "yes":
    score += 2
    findings.append("Antivirus protection is missing or outdated.")
    recommendations.append("Install or update antivirus protection.")

shadow_it = ask_yes_no("Do you use unapproved or unknown software on the system?")
if shadow_it == "yes":
    score += 1
    findings.append("Shadow IT or unapproved applications detected.")
    recommendations.append("Remove unknown or unnecessary software.")

# Step 3: Human Perimeter
guest_enabled = ask_yes_no("Is a guest account enabled on the machine?")
if guest_enabled == "yes":
    score += 2
    findings.append("Guest account is enabled.")
    recommendations.append("Disable guest accounts to reduce exposure.")

too_many_admins = ask_yes_no("Do you use admin privileges for everyday tasks?")
if too_many_admins == "yes":
    score += 2
    findings.append("Excessive administrator privilege usage detected.")
    recommendations.append("Apply least privilege and use a standard account when possible.")

poor_lock = ask_yes_no("Is screen lock disabled or too weak?")
if poor_lock == "yes":
    score += 1
    findings.append("Weak screen locking practice detected.")
    recommendations.append("Enable automatic screen lock with a short timeout.")

unsafe_storage = ask_yes_no("Do you store sensitive information in unsafe ways?")
if unsafe_storage == "yes":
    score += 1
    findings.append("Sensitive information is stored insecurely.")
    recommendations.append("Avoid storing passwords or sensitive notes in plain text.")

usb_risk = ask_yes_no("Do you connect unknown USB devices to this system?")
if usb_risk == "yes":
    score += 1
    findings.append("Risky removable media behavior detected.")
    recommendations.append("Avoid using unknown USB devices.")

# Step 4: Endpoint Hygiene
firewall_off = ask_yes_no("Is the operating system firewall disabled?")
if firewall_off == "yes":
    score += 2
    findings.append("Firewall is disabled.")
    recommendations.append("Enable the operating system firewall.")

disk_unencrypted = ask_yes_no("Is full disk encryption disabled?")
if disk_unencrypted == "yes":
    score += 2
    findings.append("Disk encryption is not enabled.")
    recommendations.append("Enable BitLocker or FileVault for data-at-rest protection.")

if score <= 3:
    risk_level = "Low"
elif score <= 8:
    risk_level = "Medium"
else:
    risk_level = "High"

print("\n--- Audit Summary ---")
print("Total Risk Score:", score)
print("Risk Level:", risk_level)

print("\nFindings:")
if findings:
    for item in findings:
        print("-", item)
else:
    print("- No major issues detected.")

print("\nRecommendations:")
if recommendations:
    for item in recommendations:
        print("-", item)
else:
    print("- No immediate action required.")