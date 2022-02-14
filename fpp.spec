Summary:	Bash Output File Picker
Name:		fpp
Version:	0.9.5
Release:	1
License:	BSD
Group:		Applications/Shells
Source0:	https://github.com/facebook/PathPicker/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b0ad45fd1789423c4fa31619d95c144c
URL:		https://facebook.github.io/PathPicker/
Requires:	python3
Requires:	python3-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_prefix}/lib/%{name}

%description
Bash Output File Picker

PathPicker parses piped input for files and presents it in a
convenient UI.

%prep
%setup -q -n PathPicker-%{version}

# remove some bsdtar junk (AppleDouble encoded Macintosh files)
# https://github.com/facebook/PathPicker/issues/174
rm -vf src/._*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_bindir}}
cp -a fpp src $RPM_BUILD_ROOT%{_appdir}
ln -s %{_appdir}/fpp $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fpp
%dir %{_appdir}
%attr(755,root,root) %{_appdir}/fpp
%{_appdir}/src
