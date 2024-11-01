################################################################################
# rpm package spec file for pdfjam-extras
#
# Copyright (c) 2022 Toby Breckon
################################################################################

Name:           pdfjam-extras
Version:        0.12
Release:        0
Summary:        a set of additional utility scripts for pdfjam
License:        GPL-2.0-only
URL:            https://github.com/tobybreckon/pdfjam-extras/
Group:          Productivity/Publishing/PDF
BuildArch:      noarch
Packager:       Toby Breckon
Requires:       bash
Requires:       pdfjam
BuildRequires:  unzip
BuildRoot:      ~/rpmbuild/
%undefine _disable_source_fetch
Source0:        https://github.com/tobybreckon/pdfjam-extras/archive/refs/heads/master.zip

################################################################################

%description
a set of additional command-line utility scripts for pdfjam

################################################################################

%prep
%setup -n  pdfjam-extras-master
echo "BUILDROOT = $RPM_BUILD_ROOT"
rm -rf $RPM_BUILD_ROOT

exit

################################################################################

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
cp bin/* $RPM_BUILD_ROOT%{_bindir}
cp man1/* $RPM_BUILD_ROOT%{_mandir}/man1/

################################################################################

%clean
rm -rf %{_builddir}/pdfjam-extras-master
rm -rf $RPM_BUILD_ROOT
rm -rf %{_sourcedir}/master.zip

################################################################################

%files
%{_bindir}/pdf180
%{_bindir}/pdf270
%{_bindir}/pdf90
%{_bindir}/pdfbook
%{_bindir}/pdfflip
%{_bindir}/pdfjam-pocketmod
%{_bindir}/pdfjam-slides3up
%{_bindir}/pdfjam-slides6up
%{_bindir}/pdfjoin
%{_bindir}/pdfnup
%{_bindir}/pdfpun
%{_mandir}/man1/pdf180.1.gz
%{_mandir}/man1/pdf270.1.gz
%{_mandir}/man1/pdf90.1.gz
%{_mandir}/man1/pdfbook.1.gz
%{_mandir}/man1/pdfflip.1.gz
%{_mandir}/man1/pdfjam-pocketmod.1.gz
%{_mandir}/man1/pdfjam-slides3up.1.gz
%{_mandir}/man1/pdfjam-slides6up.1.gz
%{_mandir}/man1/pdfjoin.1.gz
%{_mandir}/man1/pdfnup.1.gz
%{_mandir}/man1/pdfpun.1.gz

################################################################################

%changelog
* Fri Nov 1 2024 Toby Breckon <toby.breckon@durham.ac.uk> - 0.12
  - fix issue with pdfjam-pocketmod and directory output error message (credit/contributor:  Wikinaut)
* Tue Nov 1 2022 Toby Breckon <toby.breckon@durham.ac.uk> - 0.11
  - change all shebang lines in scripts to maximise cross platform/distribution compatibility
* Tue Jun 21 2022 Toby Breckon <toby.breckon@durham.ac.uk> - 0.1
  - package up the original scripts as provided from the pdfjam authors

  
################################################################################
