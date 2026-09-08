Name: buildproj
Version: 1.0
Release: 1%{?dist}
Summary: Expression evaluator with a job control plane
License: MIT

%description
Demo package for the CodeDelta build-alert stress fixture.

%build
make

%install
install -D -m 755 app %{buildroot}/usr/bin/buildproj

%files
/usr/bin/buildproj
