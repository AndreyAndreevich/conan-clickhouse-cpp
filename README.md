### Add remote
```
conan remote add my "https://api.bintray.com/conan/12345678/clickhouse-cpp"
```

### Include on conaninfo.txt
```
clickhouse-cpp/0.1@conan/testing
```

### Options:
shared: [True, False], default: shared=False

### Generators:
cmake