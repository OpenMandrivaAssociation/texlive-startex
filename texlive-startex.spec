Name:		texlive-startex
Version:	69742
Release:	1
Summary:	An XML-inspired format for student use
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/startex
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/startex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/startex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/startex.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A TeX format designed to help students write short reports and
essays. It provides the user with a suitable set of commands
for such a task. It is also more robust than plain TeX and
LaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/startex
%{_texmfdistdir}/tex/startex
%doc %{_texmfdistdir}/doc/otherformats/startex
#- source
%doc %{_texmfdistdir}/source/startex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}
