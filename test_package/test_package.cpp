#include <iostream>

#include <clickhouse/client.h>

int main(int argc, char **argv)
{
	using namespace clickhouse;

	Block block;

    auto id = std::make_shared<ColumnUInt64>();
    id->Append(1);
    id->Append(7);

	std::cout << "Clickhouse run" << std::endl;
}
