# 1-install_a_package.pp
# Install Flask version 2.1.0 using pip3

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'], # Ensure pip3 is installed first
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['python3-pip'], # Ensure pip3 is installed first
}

# Ensure python3-pip is installed
package { 'python3-pip':
  ensure => installed,
}
