
%include	/usr/lib/rpm/macros.python
%define 	module	HTMLTemplate

Summary:	Another (X)HTML template Python module
Summary(pl):	Kolejny modu³ Pythona do przetwarzania szablonów (X)HTML
Name:		python-%{module}
Version:	0.4.3
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://freespace.virgin.net/hamish.sanderson/%{module}-%{version}.tar.gz
# Source0-md5:	01dcd16ee3bc116f43d8a2c3923bac86
URL:		http://freespace.virgin.net/hamish.sanderson/htmltemplate.html
BuildRequires:	python-devel >= 2.3
Requires:	python >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTMLTemplate converts (X)HTML templates into a simple Python object
model that can be manipulated by ordinary Python scripts. Fast,
powerful and easy to use.

%description -l pl
HTMLTemplate przekszta³ca szablony (X)HTML w proste drzewo obiektów w
Pythonie, ktore mo¿e byæ przetwarzane przy pomocy skryptów pisanych w
tym jêzyku. Modu³ HTMLTemplte jest szybki, efektywny i ³atwy w u¿yciu.

%package doc
Summary:	Documentation for HTMLTemplate module
Summary(pl):	Dokumentacja do modu³u HTMLTemplate
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for HTMLTemplate Python
module.

%description doc -l pl
Pakiet zawieraj±cy dokumentacjê dla modu³u Pythona HTMLTemplate.

%package examples
Summary:	Examples for HTMLTemplate module
Summary(pl):	Przyk³ady do modu³u HTMLTemplate
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example files for HTMLTemplate Python module.

%description examples -l pl
Pakiet zawieraj±cy przyk³adowe skrypty dla modu³u Pythona HTMLTemplate.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
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
%doc Manual.txt Tutorials.txt

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
