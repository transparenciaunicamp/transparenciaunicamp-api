# -*- mode: ruby -*-
# vi: set ft=ruby :

$apt = <<SHELL

#!/usr/bin/env bash

#With this utility the progress report is nice and concise
function install {
   for i in $@; do
      echo Installing $i
      apt-get --assume-yes install "$i" > /dev/null 2>&1
  done
}

# Ensure we are using UTF-8 for everything
update-locale LANG=en_US.UTF-8 LANGUAGE=en_US.UTF-8 LC_ALL=en_US.UTF-8

start_seconds="$(date +%s)"
echo "Welcome to the initialization script!"

apt_package_check_list=(
    git
    libbz2-dev
    libffi-dev
    libncurses5-dev
    libncursesw5-dev
    libpq-dev
    libsqlite3-dev
    postgresql
    postgresql-contrib
    psycopg2
)

# Loop through each of our packages that should be installed on the system. If
# not yet installed, it should be added to the array of packages to install.
apt_package_install_list=()
for pkg in "${apt_package_check_list[@]}"; do
    package_version="$(dpkg -s $pkg 2>&1 | grep 'Version:' | cut -d " " -f 2)"
    if [[ -n "${package_version}" ]]; then
        space_count="$(expr 20 - "${#pkg}")"
        pack_space_count="$(expr 30 - "${#package_version}")"
        real_space="$(expr ${space_count} + ${pack_space_count} + ${#package_version})"
        printf " * $pkg %${real_space}.${#package_version}s ${package_version}\n"
    else
        echo " *" $pkg [not installed]
        apt_package_install_list+=($pkg)
    fi
done

# If there are any packages to be installed in the apt_package_list array,
# then we'll run `apt-get update` and then `apt-get install` to proceed.
if [[ ${#apt_package_install_list[@]} = 0 ]]; then
    echo -e "No packages to install"
else

    echo "Updating repositories..."
    apt-get update -q -y > /dev/null 2>&1

    echo "Installing build tools..."
    apt-get install -q -y build-essential > /dev/null 2>&1
    apt-get install -q -y curl > /dev/null 2>&1
    apt-get install -q -y python-software-properties > /dev/null 2>&1
    apt-get install -q -y software-properties-common > /dev/null 2>&1

    echo "Adding sources..."
    # https://launchpad.net/~git-core/+archive/ubuntu/ppa
    #add-apt-repository -y ppa:git-core/ppa > /dev/null 2>&1

    # https://github.com/nodesource/distributions
    curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash - > /dev/null 2>&1

    apt-get update -q -y > /dev/null 2>&1

    echo "Installing packages..."
    install ${apt_package_install_list[@]}

fi

end_seconds="$(date +%s)"
echo "Provisioning complete in "$(expr $end_seconds - $start_seconds)" seconds"

SHELL

$pyenv = <<SHELL

#!/usr/bin/env bash

export PYTHON_VERSION=3.5.1
export PYENV_ROOT="${HOME}/.pyenv"

if [ ! -d "${PYENV_ROOT}" ]; then

  git clone git://github.com/yyuu/pyenv.git ${PYENV_ROOT}

fi

echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
source ~/.bash_profile

# Rebuild the shim executables
pyenv install ${PYTHON_VERSION}
pyenv global ${PYTHON_VERSION}
pyenv rehash

SHELL

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_url = "https://vagrantcloud.com/ubuntu/trusty64"

  config.vm.define "transparenciaunicamp" do |base|
  end

  config.vm.hostname  = "vagrant"
  config.vm.network :forwarded_port, host: 80, guest: 80
  config.vm.network :forwarded_port, host: 8000, guest: 8000
  config.vm.network :forwarded_port, host: 8080, guest: 8080

  config.vm.provision "apt", type: "shell" do |sh|
    sh.privileged = true
    sh.inline = $apt
  end

  config.vm.provision "pyenv", type: "shell" do |sh|
    sh.privileged = false
    sh.inline = $pyenv
  end

  # Parallels-specific configuration
  config.vm.provider :parallels do |parallels, override|
      override.vm.box = "parallels/ubuntu-14.04"
      override.vm.box_url = "https://vagrantcloud.com/parallels/boxes/ubuntu-14.04"

      parallels.update_guest_tools = false
      parallels.cpus = 1
      parallels.memory = 2048
  end
end
