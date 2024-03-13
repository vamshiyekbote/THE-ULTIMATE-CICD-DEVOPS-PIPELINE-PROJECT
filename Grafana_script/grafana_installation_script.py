import subprocess

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode(), error.decode()

# Install necessary dependencies
install_dependencies_command = "sudo apt-get install -y adduser libfontconfig1 musl"
run_command(install_dependencies_command)

# Download Grafana
grafana_download_command = "wget https://dl.grafana.com/enterprise/release/grafana-enterprise_10.4.0_amd64.deb"
run_command(grafana_download_command)

# Install Grafana
grafana_install_command = "sudo dpkg -i grafana-enterprise_10.4.0_amd64.deb"
run_command(grafana_install_command)

