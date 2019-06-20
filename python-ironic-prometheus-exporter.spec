# Using Python 2 as Python 3 won't work on centos 7 because
# of missing dependencies
%global pyver 2

%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build

%global full_release ironic-%{version}

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}


Name:       openshift-ironic-prometheus-exporter
Epoch:      1
Version:    XXX
Release:    1%{?dist}
Summary:    ironic-prometheus-exporter provides a way to export hardware sensor data from ironic project in OpenStack to Prometheus
License:    ASL 2.0
URL:        https://github.com/metal3-io/ironic-prometheus-exporter

Source0:    https://github.com/metal3-io/ironic-prometheus-exporter/archive/%{commit}/%{library}-%{shortcommit}.tar.gz

BuildArch:  noarch

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-setuptools


%description
ironic-prometheus-exporter provides a way to export hardware sensor data from
ironic project in OpenStack to Prometheus. It's implemented as an
oslo-messaging notification driver to get the sensor data and a Flask
Application to export the metrics to Prometheus. It can be used not only in
metal3 but in any OpenStack deployment which includes Ironic service.

%package -n  python%{pyver}-%{library}
Summary:    ironic-prometheus-exporter provides a way to export hardware sensor data from ironic project in openstack to Prometheus
%{?python_provide:%python_provide python%{pyver}-%{library}}

Requires: python%{pyver}-pbr
Requires: python%{pyver}-stevedore >= 1.20.0
Requires: python%{pyver}-oslo-messaging >= 9.4.0
Requires: python%{pyver}-flask >= 0.12.3
Requires: python%{pyver}-prometheus_client >= 0.6.0
Requires: python%{pyver}-oslo-config
Requires: python%{pyver}-configparser

%description -n python%{pyver}-%{library}
ironic-prometheus-exporter provides a way to export hardware sensor data from
ironic project in OpenStack to Prometheus. It's implemented as an
oslo-messaging notification driver to get the sensor data and a Flask
Application to export the metrics to Prometheus. It can be used not only in
metal3 but in any OpenStack deployment which includes Ironic service.

%prep
%autosetup -n %{module}-%{upstream_version} -S git

%build
%{pyver_build}

%install
%{pyver_install}

%files -n python%{pyver}-%{library}
%license LICENSE
%{pyver_sitelib}/%{module}
%{pyver_sitelib}/%{module}-*.egg-info
%exclude %{pyver_sitelib}/%{module}/tests

%changelog
