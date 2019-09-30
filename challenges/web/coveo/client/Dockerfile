FROM microsoft/dotnet:2.2-sdk AS builder
LABEL name="UnitedCTF client"

ARG protocol="http"
ARG uri="localhost"
ARG port=3000

RUN apt-get update \
  && apt-get install -y \
    zip
WORKDIR /app
RUN mkdir output

# copy csproj and restore as distinct layers
COPY *.csproj ./
RUN dotnet restore
# copy and build everything else
COPY . ./
RUN sed -i "s+%%URL%%+${protocol}://${uri}:${port}+g" QueryModel.cs
RUN dotnet publish -r osx-x64 -c Release --self-contained
RUN zip -r -D output/osx.zip ./bin/Release/netcoreapp2.2/osx-x64/publish/*
RUN dotnet publish -r win-x64 -c Release --self-contained
RUN zip -r -D output/win.zip ./bin/Release/netcoreapp2.2/win-x64/publish/*
RUN dotnet publish -r linux-x64 -c Release --self-contained
RUN zip -r -D output/linux.zip ./bin/Release/netcoreapp2.2/linux-x64/publish/*

FROM node:argon
WORKDIR /serve
COPY --from=builder /app/output .

RUN npm install -g http-server

EXPOSE 8080
CMD [ "http-server" ]