%global tl_name coolthms
%global tl_revision 29062

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Reference items in a theorem environment
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/coolthms
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/coolthms.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/coolthms.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/coolthms.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the means to directly reference items of lists
nested in theorem-like environments (e.g., as 'Theorem 1 a'). The
package extends the ntheorem and cleveref packages. The package also
provides other theorem markup commands.

