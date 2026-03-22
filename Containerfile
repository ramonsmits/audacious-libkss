FROM fedora:43 AS build
RUN dnf install -y audacious-devel cmake gcc g++ make && dnf clean all

COPY . /build/audacious-libkss
WORKDIR /build/audacious-libkss

RUN cmake -B build -DCMAKE_BUILD_TYPE=Release && \
    cmake --build build -j$(nproc)

FROM scratch
COPY --from=build /build/audacious-libkss/build/kss-libkss.so /kss-libkss.so
