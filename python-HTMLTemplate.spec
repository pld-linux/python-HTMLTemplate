
%define 	module	HTMLTemplate

Summary:	Another (X)HTML template Python module
Summary(pl.UTF-8):	Kolejny moduł Pythona do przetwarzania szablonów (X)HTML
Name:		python-%{module}
Version:	1.4.1
Release:	4
License:	LGPL
Group:		Libraries/Python
Source0:	http://freespace.virgin.net/hamish.sanderson/%{module}-%{version}.tar.gz
# Source0-md5:	74bbaee9b851b17b5c5cd1658ea42897
URL:		http://freespace.virgin.net/hamish.sanderson/htmltemplate.html
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTMLTemplate converts (X)HTML templates into a simple Python object
model that can be manipulated by ordinary Python scripts. Fast,
powerful and easy to use.

%description -l pl.UTF-8
HTMLTemplate przekształca szablony (X)HTML w proste drzewo obiektów w
Pythonie, które może być przetwarzane przy pomocy skryptów pisanych w
tym języku. Moduł HTMLTemplte jest szybki, efektywny i łatwy w użyciu.

%package doc
Summary:	Documentation for HTMLTemplate module
Summary(pl.UTF-8):	Dokumentacja do modułu HTMLTemplate
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for HTMLTemplate Python
module.

%description doc -l pl.UTF-8
Pakiet zawierający dokumentację dla modułu Pythona HTMLTemplate.

%package examples
Summary:	Examples for HTMLTemplate module
Summary(pl.UTF-8):	Przykłady do modułu HTMLTemplate
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example files for HTMLTemplate Python module.

%description examples -l pl.UTF-8
Pakiet zawierający przykładowe skrypty dla modułu Pythona HTMLTemplate.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_examplesdir}/%{name}-%{version}}

%py_install \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

cp -a Examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{py_sitescriptdir}/HTMLTemplate.py[oc]

%files doc
%defattr(644,root,root,755)
%doc Documentation/{Manual.txt,Tutorial_1.txt,Tutorial_2.txt,FAQ.txt}

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
