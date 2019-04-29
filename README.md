### Export sources:
`conan export . demo/testing`\
`conan install clickhouse-cpp/0.1@demo/testing --build`\
`conan test test_package clickhouse-cpp/0.1@demo/testing`

### Include on conaninfo.txt
clickhouse-cpp/0.1@demo/testing

### Options:
shared: [True, False], default: shared=False

### Generators:
cmake