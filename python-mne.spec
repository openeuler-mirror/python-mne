%global _empty_manifest_terminate_build 0
Name:		python-mne
Version:	0.24.1
Release:	1
Summary:	MNE-Python project for MEG and EEG data analysis.
License:	BSD-3-Clause
URL:		https://github.com/mne-tools/mne-python
Source0:	https://files.pythonhosted.org/packages/b0/64/8cd2716407139822b268ed65662ec8ef0880aa0cd86c715b698b49a4c7e7/mne-0.24.1.tar.gz
BuildArch:	noarch

Requires:	python3-numpy
Requires:	python3-scipy
Requires:	python3-tqdm
Requires:	python3-pooch
Requires:	python3-pytest
Requires:	python3-pytest-cov
Requires:	python3-pytest-timeout
Requires:	python3-pytest-harvest
Requires:	python3-flake8
Requires:	python3-flake8-array-spacing
Requires:	python3-numpydoc
Requires:	python3-codespell
Requires:	python3-pydocstyle
Requires:	python3-check-manifest
Requires:	python3-twine
Requires:	python3-wheel
Requires:	python3-pooch
Requires:	python3-nitime
Requires:	python3-nbclient
Requires:	python3-sphinx-gallery
Requires:	python3-eeglabio
Requires:	python3-EDFlib-Python
Requires:	python3-imageio-ffmpeg

%description
MNE-Python software is an open-source Python package for exploring, visualizing, and analyzing 
human neurophysiological data such as MEG, EEG, sEEG, ECoG, and more. It includes modules 
for data input/output, preprocessing, visualization, source estimation, time-frequency 
analysis, connectivity analysis, machine learning, and statistics.

%package -n python3-mne
Summary:	MNE-Python project for MEG and EEG data analysis.
Provides:	python-mne
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-mne
MNE-Python software is an open-source Python package for exploring, visualizing, and analyzing 
human neurophysiological data such as MEG, EEG, sEEG, ECoG, and more. It includes modules 
for data input/output, preprocessing, visualization, source estimation, time-frequency 
analysis, connectivity analysis, machine learning, and statistics.

%package help
Summary:	Development documents and examples for mne
Provides:	python3-mne-doc
%description help
MNE-Python software is an open-source Python package for exploring, visualizing, and analyzing 
human neurophysiological data such as MEG, EEG, sEEG, ECoG, and more. It includes modules 
for data input/output, preprocessing, visualization, source estimation, time-frequency 
analysis, connectivity analysis, machine learning, and statistics.

%prep
%autosetup -n mne-0.24.1

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-mne -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Fri Dec 17 2021 Python_Bot <Python_Bot@openeuler.org> - 0.24.1-1
- Package Init

