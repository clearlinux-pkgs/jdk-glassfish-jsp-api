Name     : jdk-glassfish-jsp-api
Version  : 2.0
Release  : 1
URL      : http://repo.maven.apache.org/maven2/javax/servlet/jsp-api/2.0/jsp-api-2.0.jar
Source0  : http://repo.maven.apache.org/maven2/javax/servlet/jsp-api/2.0/jsp-api-2.0.jar
Source1  : http://repo.maven.apache.org/maven2/javax/servlet/jsp-api/2.0/jsp-api-2.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-glassfish-jsp-api-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-glassfish-jsp-api package.
Group: Data

%description data
data components for the jdk-glassfish-jsp-api package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/glassfish-jsp-api.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/glassfish-jsp-api.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/glassfish-jsp-api.xml \
%{buildroot}/usr/share/maven-poms/glassfish-jsp-api.pom \
%{buildroot}/usr/share/java/glassfish-jsp-api.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/glassfish-jsp-api.jar
/usr/share/maven-metadata/glassfish-jsp-api.xml
/usr/share/maven-poms/glassfish-jsp-api.pom
