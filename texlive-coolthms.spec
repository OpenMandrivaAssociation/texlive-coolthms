Name:		texlive-coolthms
Version:	29062
Release:	2
Summary:	Reference items in a theorem environment
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/coolthms
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coolthms.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coolthms.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coolthms.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means to directly reference items of
lists nested in theorem-like environments (e.g., as 'Theorem 1
a'). The package extends the ntheorem and cleveref packages.
The package also provides other theorem markup commands.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/coolthms/coolthms.sty
%doc %{_texmfdistdir}/doc/latex/coolthms/README
%doc %{_texmfdistdir}/doc/latex/coolthms/coolthms.pdf
#- source
%doc %{_texmfdistdir}/source/latex/coolthms/coolthms.dtx
%doc %{_texmfdistdir}/source/latex/coolthms/coolthms.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
