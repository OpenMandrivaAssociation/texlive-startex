%global tl_name startex
%global tl_revision 69742

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.04
Release:	%{tl_revision}.1
Summary:	An XML-inspired format for student use
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/formats/startex
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/startex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/startex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/startex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A TeX format designed to help students write short reports and essays.
It provides the user with a suitable set of commands for such a task. It
is also more robust than plain TeX and LaTeX.

