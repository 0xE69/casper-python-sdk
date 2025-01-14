import argparse
import asyncio

from pycspr import NodeClient
from pycspr import NodeConnection


# CLI argument parser.
_ARGS = argparse.ArgumentParser("How to consume node SSE events demo.")

# CLI argument: host address of target node - defaults to CCTL node 1.
_ARGS.add_argument(
    "--node-host",
    default="localhost",
    dest="node_host",
    help="Host address of target node.",
    type=str,
    )

# CLI argument: Node API JSON-RPC port - defaults to 11101 @ CCTL node 1.
_ARGS.add_argument(
    "--node-port-rpc",
    default=11101,
    dest="node_port_rpc",
    help="Node API JSON-RPC port.  Typically 7777 on most nodes.",
    type=int,
    )

# CLI argument: Node API SSE port - defaults to 18101 @ CCTL node 1.
_ARGS.add_argument(
    "--node-port-sse",
    default=18101,
    dest="node_port_sse",
    help="Node API SSE port.  Typically 9999 on most nodes.",
    type=int,
    )


async def main(args: argparse.Namespace):
    """Main entry point.

    :param args: Parsed command line arguments.

    """
    # Set node client.
    client = _get_client(args)

    # Await until 2 blocks have been added to linear chain.
    print("awaiting 2 blocks ...")
    block_height = client.get_block_height()
    await client.await_n_blocks(2)
    assert client.get_block_height() == block_height + 2

    # Await until 1 consensus era has elapsed.
    print("awaiting 1 era ...")
    era_height = client.get_era_height()
    await client.await_n_eras(1)
    assert client.get_era_height() == era_height + 1

    # Await until a block in the future.
    future_block_height = client.get_block_height() + 2
    print(f"awaiting until block {future_block_height} ...")
    await client.await_until_block_n(future_block_height)
    assert client.get_block_height() == future_block_height

    # Await until a consensus era in the future.
    future_era_height = client.get_era_height() + 1
    print(f"awaiting until era {future_era_height} ...")
    await client.await_until_era_n(future_era_height)
    assert future_era_height == client.get_era_height()


def _get_client(args: argparse.Namespace) -> NodeClient:
    """Returns a pycspr client instance.

    """
    return NodeClient(NodeConnection(
        host=args.node_host,
        port_rpc=args.node_port_rpc,
        port_sse=args.node_port_sse
    ))


# Entry point.
if __name__ == "__main__":
    asyncio.run(main(_ARGS.parse_args()))
