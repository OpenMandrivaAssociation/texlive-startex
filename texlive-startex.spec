# revision 15878
# category Package
# catalog-ctan /macros/startex
# catalog-date 2008-12-31 20:54:46 +0100
# catalog-license pd
# catalog-version 1.04
Name:		texlive-startex
Version:	1.04
Release:	1
Summary:	An XML-inspired format for student use
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/startex
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/startex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/startex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/startex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A TeX format designed to help students write short reports and
essays. It provides the user with a suitable set of commands
for such a task. It is also more robust than plain TeX and
LaTeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/startex/stxglo.ist
%{_texmfdistdir}/makeindex/startex/stxind.ist
%{_texmfdistdir}/tex/startex/base/a4-article.stx
%{_texmfdistdir}/tex/startex/base/article.stx
%{_texmfdistdir}/tex/startex/base/ifi-article.stx
%{_texmfdistdir}/tex/startex/base/ifi-artikkel.stx
%{_texmfdistdir}/tex/startex/base/startex.lan
%{_texmfdistdir}/tex/startex/base/startex.tex
%doc %{_texmfdistdir}/doc/otherformats/startex/base/guide.pdf
%doc %{_texmfdistdir}/doc/otherformats/startex/base/ideas.pdf
%doc %{_texmfdistdir}/doc/otherformats/startex/base/startex.pdf
#- source
%doc %{_texmfdistdir}/source/startex/base/INSTALL
%doc %{_texmfdistdir}/source/startex/base/README
%doc %{_texmfdistdir}/source/startex/base/startex.bib
%doc %{_texmfdistdir}/source/startex/base/startex.dtx
%doc %{_texmfdistdir}/source/startex/base/startex.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
