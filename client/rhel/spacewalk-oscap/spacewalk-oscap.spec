%if 0%{?fedora}
%global build_py3   1
%global default_py3 1
%endif

%define pythonX %{?default_py3: python3}%{!?default_py3: python2}

Name:		spacewalk-oscap
Version:	2.8.2
Release:	1%{?dist}
Summary:	OpenSCAP plug-in for rhn-check

Group:		Applications/System
License:	GPLv2
URL:		https://github.com/spacewalkproject/spacewalk
Source0:	https://github.com/spacewalkproject/spacewalk/archive/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
BuildRequires:  libxslt
%if 0%{?rhel}
Requires: openscap-utils
%else
Requires:	openscap-scanner
%endif
Requires:	libxslt
Requires:       %{pythonX}-%{name}

%description
spacewalk-oscap is a plug-in for rhn-check. With this plugin, user is able
to run OpenSCAP scan from Spacewalk or Red Hat Satellite server.

%package -n python2-%{name}
Summary:	OpenSCAP plug-in for rhn-check
%{?python_provide:%python_provide python2-%{name}}
Requires:       spacewalk-oscap
Requires:       rhnlib >= 0:2.5.78-1
Requires:       python2-rhn-check
BuildRequires:	python-devel
BuildRequires:	rhnlib
%description -n python2-%{name}
Python 2 specific files for %{name}.

%if 0%{?build_py3}
%package -n python3-%{name}
Summary:	OpenSCAP plug-in for rhn-check
%{?python_provide:%python_provide python3-%{name}}
Requires:       spacewalk-oscap
Requires:       python3-rhnlib >= 0:2.5.78-1
Requires:       python3-rhn-check
BuildRequires:	python3-devel
BuildRequires:	python3-rhnlib
%description -n python3-%{name}
Python 3 specific files for %{name}.
%endif

%prep
%setup -q


%build
make -f Makefile.spacewalk-oscap


%install
rm -rf $RPM_BUILD_ROOT
make -f Makefile.spacewalk-oscap install PREFIX=$RPM_BUILD_ROOT PYTHONPATH=%{python_sitelib}
%if 0%{?build_py3}
make -f Makefile.spacewalk-oscap install PREFIX=$RPM_BUILD_ROOT PYTHONPATH=%{python3_sitelib}
%endif

%clean
rm -rf $RPM_BUILD_ROOT


%files
%config  /etc/sysconfig/rhn/clientCaps.d/scap
%{_datadir}/openscap/xsl/xccdf-resume.xslt
%if 0%{?suse_version}
%dir /etc/sysconfig/rhn
%dir /etc/sysconfig/rhn/clientCaps.d
%dir %{_datadir}/openscap
%dir %{_datadir}/openscap/xsl
%endif

%files -n python2-%{name}
%{python_sitelib}/actions/scap.*

%if 0%{?build_py3}
%files -n python3-%{name}
%{python3_sitelib}/actions/scap.*
%{python3_sitelib}/actions/__pycache__/scap.*
%endif

%changelog
* Fri Sep 22 2017 Michael Mraka <michael.mraka@redhat.com> 2.8.2-1
- install files into python_sitelib/python3_sitelib
- split spacewalk-oscap into python2/python3 specific packages

* Wed Sep 06 2017 Michael Mraka <michael.mraka@redhat.com> 2.8.1-1
- purged changelog entries for Spacewalk 2.0 and older
- Bumping package versions for 2.8.

* Thu May 18 2017 Tomas Kasparek <tkasparek@redhat.com> 2.7.1-1
- 1451778 - require openscap-utils on rhel for backward compatibility
- Updated links to github in spec files
- Migrating Fedorahosted to GitHub
- Bumping package versions for 2.7.

* Mon Sep 12 2016 Ondrej Gajdusek <ogajduse@redhat.com> 2.6.1-1
- Increasing required version of rhnlib in due to ImportError module i18n in
  scap.py
- Bumping package versions for 2.6.

* Mon May 23 2016 Gennadii Altukhov <galt@redhat.com> 2.5.3-1
- convert code to work in python 2/3

* Fri May 20 2016 Grant Gainey 2.5.2-1
- spacewalk-oscap: build on openSUSE

* Fri Jan 22 2016 Tomas Lestach <tlestach@redhat.com> 2.5.1-1
- 1232596 - still require openscap-utils on RHEL5
- Bumping package versions for 2.5.

* Fri Jun 19 2015 Tomas Kasparek <tkasparek@redhat.com> 2.4.1-1
- rhbz#1232596: Require just openscap-scanner package everywhere
- Bumping package versions for 2.4.

* Mon Sep 22 2014 Matej Kollar <mkollar@redhat.com> 2.3.1-1
- 1107841 - Avoid creating profile with empty id
- Typo
- Retab
- Bumping package versions for 2.3.
- Bumping package versions for 2.2.

