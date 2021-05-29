const delay = millis => new Promise((resolve, reject) => {
    setTimeout(_ => resolve(), millis)
});

const userAccount = await wax.login();
account = userAccount;


async function mine() {
    let mine_work = await background_mine(account)
    unityInstance.SendMessage('Controller', 'Server_Response_Mine', JSON.stringify(mine_work));

    //await delay(25000)

    const mine_data = { miner: mine_work.account, nonce: mine_work.rand_str };
    const actions = [{
        account: mining_account, name: 'mine',
        authorization: [{ actor: mine_work.account, permission: 'active' }],
        data: mine_data
    }];
    // console.group('wax mining')
    console.log('## wax transact', actions);

    try {
        console.log('## wax mining...');
        const result = await wax.api.transact({ actions }, { blocksBehind: 3, expireSeconds: 90, })
        console.log('## wax result', result);

        if (!result || !result.processed) return

        let amounts = new Map();
        for (const at of result.processed.action_traces) {
            for (const it of at.inline_traces) {
                const mine_amount = it.act.data.quantity;
                if (!mine_amount) continue

                console.log(`## wax ${mine_work.account} Mined ${mine_amount}`);
                if (amounts.has(it.act.data.to)) {
                    let obStr = amounts.get(it.act.data.to);
                    obStr = obStr.substring(0, obStr.length - 4);
                    let nbStr = it.act.data.quantity;
                    nbStr = nbStr.substring(0, nbStr.length - 4);
                    let balance = (parseFloat(obStr) + parseFloat(nbStr)).toFixed(4);
                    amounts.set(it.act.data.to, balance.toString() + ' TLM');
                } else {
                    amounts.set(it.act.data.to, it.act.data.quantity);
                }
            }
        }
        console.log(`## unity response ${mine_work.account} claim...`);
        unityInstance.SendMessage('Controller', 'Server_Response_Claim', amounts.get(mine_work.account));
    } catch (err) {
        console.log(`## unity response ${mine_work.account} mine error...`);
        console.error(err);
        unityInstance.SendMessage('ErrorHandler', 'Server_Response_SetErrorData', err.message);
        console.log('## mine sleeping 20s.')
        await delay(20000)
    }

    var balance = await getBalance(account, wax.api.rpc);
    console.log('balance (after mined): ' + balance);

}



async function rec(){
    minedelay = await getMineDelay(account);
    if (minedelay === 0) {
        mine()
        await delay(60000)
    }
    minedelay = await getMineDelay(account);
    await delay(minedelay + 3000)
    rec()
}

